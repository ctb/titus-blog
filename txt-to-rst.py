#! /usr/bin/env python
# TODO: images

import sys, os, stat, datetime

filename = sys.argv[1]
todir = sys.argv[2]

assert filename.endswith('.txt')

new_filename = os.path.basename(filename[:-4]) + '.rst'
new_filename = os.path.join(todir, new_filename)

print 'testing', new_filename
assert not os.path.exists(new_filename), new_filename

statinfo = os.stat(filename)
pub_date = datetime.date.fromtimestamp(statinfo.st_mtime)

infp = open(filename)
outfp = open(new_filename, 'w')

title = infp.readline().strip()
tags = infp.readline().strip()
if tags.startswith('#tags'):
    tags = '# tags' + tags[6:]

assert not tags or tags.startswith('# tags'), (tags, filename)
tags = tags[6:].strip()

###

catlist = {}
for line in open('cats.txt'):
    tag, weight, cat = line.split()
    weight = int(weight)
    catlist[tag] = (cat, weight)

best_w = 0
best_cat = 'misc'
for tag in tags.split(','):
    cat, w = catlist.get(tag, ('misc', 0))
    if w > best_w:
        best_cat = cat

###

print >>outfp, title
print >>outfp, '#' * len(title)
print >>outfp, ''
print >>outfp, ':author: C\. Titus Brown'
if tags:
    print >>outfp, ':tags:', tags
print >>outfp, ':date:', pub_date.isoformat()
print >>outfp, ':slug:', os.path.basename(filename[:-4])
print >>outfp, ':category:', best_cat
print >>outfp, ''

for line in infp:
    outfp.write(line)

outfp.close()

#Set just the modification time:
os.utime(new_filename, (os.path.getatime(new_filename), statinfo.st_mtime))

###

if 1:
    fp = open('rewrite.txt', 'a')
    old_path, old_end = os.path.split(filename)
    _, old_path = os.path.split(old_path)
    old_path = os.path.join(old_path, old_end[:-4])
    new_path = os.path.basename(filename[:-4])

    print >>fp, 'RewriteRule ^/blog/%s.*$\t/blog/%s.html\t[R]' % (old_path, new_path,)

if 0:
    fp = open('taglist.txt', 'a')
    for tag in tags.split(','):
        print >>fp, tag.strip()
