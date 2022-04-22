Title: Storing 64-bit unsigned integers in SQLite databases, for fun and profit
Date: 2022-04-22
Category: science
Tags: sourmash, sqlite
Slug: 2022-storing-ulong-in-sqlite-sourmash
Authors: C. Titus Brown
Summary: Storing unsigned longs in SQLite is possible, and can be fast.

## The problem: storing *and querying* lots of 64-bit unsigned integers

For the past ~6 years, we've been going down quite a rabbit hole with hashing based sequence search, using a [MinHash](https://en.wikipedia.org/wiki/MinHash)-derived approach called FracMinHash. (You can read more about FracMinHash [here](https://www.biorxiv.org/content/10.1101/2022.01.11.475838), but it's essentially a bottom-sketch version of ModHash.) This is all implemented in [the sourmash software](https://sourmash.readthedocs.io/), a Python and Rust-based command-line bioinformatics toolkit.

The basic idea is that we take long DNA sequences, extract sub-sequences of a fixed length (say k=31), hash them, and then sketch them by retaining only those that fall below a certain threshold value. Then we search for matches between sketches based on number of overlapping hashes. This is a proxy for the number of overlapping k=31 subsequences, which is in turn convertible into various sequence similarity metrics.

The scale of the problems we're tackling is pretty big. As one example, we have a database (Genbank bacterial) with 1.15 million buckets of hashes, containing a total of 4.6 billion hashes across these buckets (representing approximately 4.6 trillion original k-mers). So we need to do moderately clever things to store them and search them quickly.

We already have a variety of formats for storing and querying sketch collections, including straight up zip files that contain JSON-serialized sketches, a custom disk-based [Sequence Bloom Trees](https://www.nature.com/articles/nbt.3442), and an inverted index that lives in memory. The inverted index turns out to be fast once loaded, but serialization is ...not that great, and memory consumption is very high. This is something I wanted to fix!

I've had [a long-time love of SQLite](http://ivory.idyll.org/blog/storing-and-retrieving-sequences.html), the tiny little embedded database engine that is just ridiculously fast, and I decided to figure out how to store _and query_ our sketches in SQLite.

## Using SQLite to store 64-bit unsigned integers: a first attempt

The challenge I faced here was that our sketches are composed of 64-bit unsigned integers, and SQLite _does not store_ 64-bit unsigned ints natively. But this is exactly what I needed!

Enter type converters! I found two really nice resources on automatically converting 64-bit uints into data types that SQLite could handle: [this stackoverflow post, "Python int too large to convert to SQLite INTEGER"](https://stackoverflow.com/questions/57464671/peewee-python-int-too-large-to-convert-to-sqlite-integer), and this great [tutorial from wellsr.com, Adapting and Converting SQLite Data Types for Python](https://wellsr.com/python/adapting-and-converting-sqlite-data-types-for-python/).

In brief, I swiped code from the stackoverflow answer to do the following:

* write a function that, for any hash value larger than 2**63-1, converts numbers into a hex string;
* write the opposite function that converts hex strings back to numbers;
* register these functions as adapters on a SQLite data type to automatically run for every column of that type.

This works because SQLite has a really flexible internal typing system where it can store basically anything as a string, no matter the official column type.

The python code looks like this:

```python
MAX_SQLITE_INT = 2 ** 63 - 1
sqlite3.register_adapter(
    int, lambda x: hex(x) if x > MAX_SQLITE_INT else x)
sqlite3.register_converter(
    'integer', lambda b: int(b, 16 if b[:2] == b'0x' else 10))
```

and when you connect to the database, you can tell SQLite to pay attention to those adapters like so:

```python
conn = sqlite3.connect(dbfile,
    detect_types=sqlite3.PARSE_DECLTYPES)
```

Then you define your tables in SQLite,

```sql
CREATE TABLE IF NOT EXISTS hashes
    (hashval INTEGER NOT NULL,
    sketch_id INTEGER NOT NULL,
    FOREIGN KEY (sketch_id) REFERENCES sketches (id))
    
CREATE TABLE IF NOT EXISTS sketches
  (id INTEGER PRIMARY KEY,
   name TEXT,
   ...)
```

and you can do all the querying you want, and large integers will be converted into hex strings, and life is good. Right?

This code actually worked fine! Except for one problem.

**It was very slow.** One key to making relational databases in general (and SQLite in specific) fast is to use indices, and these INTEGER columns could no longer be indexed as INTEGER columns because they contained hex strings! Which means that once databases got big, well, basically searching and retrieval was too slow to be useful.

This code was perfectly functional and lives on in [some commits](https://github.com/sourmash-bio/sourmash/blob/3259fbddf6c33b6093bea2717a4e24642145a32d/src/sourmash/sqlite_index.py), but it wasn't fast enough to be used for production code.

Unfortunately (or fortunately?), I was now _in it_. I'd sunk enough time into this problem already, and had enough functioning code and tests, that I decided to keep on going. See: [sunk cost fallacy](https://en.wikipedia.org/wiki/Sunk_cost).

## Storing 64-bit unsigned integers *efficiently* in SQLite

I wasn't actually convinced that SQLite could do it efficiently, so [I asked on Twitter](https://twitter.com/ctitusbrown/status/1490695385781661697) about alternative approaches. Among a variety of responses, @jgoldschrafe [said something very important that resonated](https://twitter.com/jgoldschrafe/status/1490700497988329485):

>SQLite isn't a performance monster for complex use cases, but should be absolutely fine for this.

and that gave me the courage to stay the course and work on a SQLite-based resolution.

The next key was an idea that I had toyed with, based on hints [here](https://sqlite-users.sqlite.narkive.com/hlY9vnL7/sqlite-storing-unsigned-64-bit-values) and then [confirmed](https://twitter.com/jgoldschrafe/status/1490701880099590146) by the still-awesome @jgoldschrafe - I didn't need _more_ than 64 bits, and I just needed to do searching based on equality. So I could convert unsigned 64-bit ints into signed 64-bit numbers, shove them into the database, and do equality testing between a query and the hashvals. As long as I was doing the conversion systematically, it would all work! 

I ended up writing two adapter functions that I call in Python code for the relevant values (_not_ using the SQLite type converter registry) -
```python
MAX_SQLITE_INT = 2 ** 63 - 1
convert_hash_to = lambda x: BitArray(uint=x, length=64).int if x > MAX_SQLITE_INT else x
convert_hash_from = lambda x: BitArray(int=x, length=64).uint if x < 0 else x
```

Note here I am using the lovely [bitstring package](https://pypi.org/project/bitstring/) so that I don't have to think hard about bit twiddling (although that's a possible optimization now that I have everything locked down with tests).

The SQL schema I am using looks like this:

```sql
CREATE TABLE IF NOT EXISTS sketches
  (id INTEGER PRIMARY KEY,
   name TEXT,
   ...)
  
CREATE TABLE IF NOT EXISTS sourmash_hashes (
   hashval INTEGER NOT NULL,
   sketch_id INTEGER NOT NULL,
   FOREIGN KEY (sketch_id) REFERENCES sourmash_sketches (id)
)
```

and I also build three indices, that correspond to the various kinds of queries I want to do -

```sql
CREATE INDEX IF NOT EXISTS sourmash_hashval_idx ON sourmash_hashes (
   hashval,
   sketch_id
)
CREATE INDEX IF NOT EXISTS sourmash_hashval_idx2 ON sourmash_hashes (
   hashval
)
CREATE INDEX IF NOT EXISTS sourmash_sketch_idx ON sourmash_hashes (
   sketch_id
)
```

One of the design decisions I made midway through this PR was to allow duplicate hashvals in `sourmash_hashes` - since different sketches can share hashvals with other sketches, we have to either do things this way, or have another intermediate table that links unique hashvals to potentially multiple sketch_ids. It just seemed simpler to have hashvals be non-unique, and instead build an index for the possible queries. (I might revisit this later, now that I can refactor fearlessly ;).

At this point, insertion is now easy:

```python
sketch_id = ...

# insert all the hashes
hashes_to_sketch = []
for h in ss.minhash.hashes:
    hh = convert_hash_to(h)
    hashes_to_sketch.append((hh, sketch_id))

c.executemany("INSERT INTO sourmash_hashes (hashval, sketch_id) VALUES (?, ?)",
              hashes_to_sketch)
```

and retrieval is similarly simple:
```python
sketch_id = ...

c.execute(f"SELECT hashval FROM sourmash_hashes WHERE sourmash_hashes.sketch_id=?", sketch_id)

for hashval, in c:
    hh = convert_hash_from(hashval)
    minhash.add_hash(hh)
```

So this was quite effective for storing the sketches in SQLite! I could perfectly reconstruct sketches after a round-trip through SQLite, which was a great first step.

Next question: could I quickly _search_ the hashes as an inverted index? That is, could I find sketches based on querying with hashes, rather than (as above) using `sketch_id` to retrieve hashes for an already identified sketch?

## Matching on 64-bit unsigned ints in SQLite

This ended up being pretty simple!

To query with a collection of hashes, I set up a temporary table containing the query hashes, and then do a join on exact value matching. Conveniently, this doesn't care whether the values in the database are signed or not - it just cares if the bit patterns are equal!

The code, for a cursor c:

```python
def _get_matching_sketches(self, c, hashes, max_hash):
        """
        For hashvals in 'hashes', retrieve all matching sketches,
        together with the number of overlapping hashes for each sketch.
        """
        c.execute("DROP TABLE IF EXISTS sourmash_hash_query")
        c.execute("CREATE TEMPORARY TABLE sourmash_hash_query (hashval INTEGER PRIMARY KEY)")

        hashvals = [ (convert_hash_to(h),) for h in hashes ]
        c.executemany("INSERT OR IGNORE INTO sourmash_hash_query (hashval) VALUES (?)",
                      hashvals)

        c.execute(f"""
        SELECT DISTINCT sourmash_hashes.sketch_id,COUNT(sourmash_hashes.hashval) as CNT
        FROM sourmash_hashes, sourmash_hash_query
        WHERE sourmash_hashes.hashval=sourmash_hash_query.hashval
        GROUP BY sourmash_hashes.sketch_id ORDER BY CNT DESC
        """, template_values)

        return c
```

As a side benefit, this query orders the results by the size of overlap between sketches, which leads to some pretty nice and efficient thresholding code.

## Benchmarking!!

I'll just say that performance is definitely acceptable - the below benchmarks compare sqldb against our other database formats. The database we're searching is a collection of 48,000 sketches with 161 million total hashes - GTDB RS202, if you're curious :).

For 53.9k query hashes, with 19.0k found in the database, the SQLite implementation is nice and fast, albeit with a large disk footprint:

| db format | db size | time | memory |
| -------- | -------- | -------- | -------- |
| sqldb | 15 GB | 28.2s | 2.6 GB |
| sbt | 3.5 GB | 2m 43s | 2.9 GB |
| zip | 1.7 GB | 5m 16s | 1.9 GB |

For larger queries, with 374.6k query hashes, where we find 189.1k in the database, performance evens out a bit:

| db format | db size | time | memory |
| -------- | -------- | -------- | -------- |
| sqldb | 15 GB | 3m 58s | 9.9 GB |
| sbt | 3.5 GB | 7m 33s | 2.6 GB  |
| zip | 1.7 GB | 5m 53s | 2.0 GB |

Note that zip file searches don't use any indexing at all, so the search is linear and it's expected that the time will more or less be the same for  regardless of the query. And SBTs are not really meant for this use case, but they are the other "fast search" database we have, so I benchmarked them anyway.

(There are lots of nuances to what we're doing here and I think I mostly understand these performance numbers; see [the benchmarking issue](https://github.com/sourmash-bio/sourmash/issues/1958) for my thoughts.)

The really nice thing is that for our motivating use case, looking hashes up in a reverse index to correlate with other labels, the performance with SQLite is _much_ better than our current JSON-on-disk/in-memory search format.

For 53.9k query hashes, we get:

| lca db format | db size | time | memory |
| -------- | -------- | -------- | -------- |
| SQL | 1.6 GB | 20s | 380 MB |
| JSON | 175 MB | 1m 21s | 6.2 GB |

which is frankly excellent - for 8x increase in disk size, we get 4x faster query and 16x lower memory usage! (The in-memory performance includes loading from disk, which is the main reason it's so terrible.)

## Further performance improvements?

I'm still pretty exhausted from this coding odyssey (> 250 commits, ending with nearly 3000 lines of code added or changed), so I'm leaving some work for the future. Most specifically, we'd like to benchmark having multiple _readers_ read from the database at once, for e.g. Web server backends. I expect it to work pretty well for that but we'll need to check.

I do use the following PRAGMAs for configuration, and I'm wondering if I should spend time trying out different parameters; this is mostly a database built around writing once, and reading many times. Advice welcome :).

```sql
PRAGMA cache_size=10000000
PRAGMA synchronous = OFF
PRAGMA journal_mode = MEMORY
PRAGMA temp_store = MEMORY
```

## Concluding thoughts

The second solution above is the code that is in [my current pull request](https://github.com/sourmash-bio/sourmash/pull/1808), and I expect it will eventually be merged into sourmash and released as part of sourmash v4.4.0. It's fully integrated into sourmash (with a much broader range of use cases than I explained above ;), and I'm pretty happy with it. There's actually a whole 'nother story about manifests that motivated some part of the above; you can read about that [here](https://github.com/sourmash-bio/sourmash/issues/1930).

I'm not planning on revisiting reverse indices in sourmash anytime soon, but we are starting to think more seriously about better (...non-JSON ways) of serializing sketches. Avro looks interesting, and there are some fast columnar formats like Arrow and Parquet; see [this issue](https://github.com/sourmash-bio/sourmash/issues/1262) for our notes.

Anyway, so that's my SQLite odyssey. Thoughts welcome!

--titus
