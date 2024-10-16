Title: Why Rust is an increasingly beloved part of my programming toolbox
Date: 2024-10-16
Category: programming
Tags: rust, python, sourmash, branchwater
Slug: 2024-why-i-like-rust
Authors: C. Titus Brown
Summary: Rust is nice!

Hi, I'm Titus. I'm a prof at UC Davis who writes scientific software for biological data analysis of very, very large data sets.  And I really like Rust, especially in combination with Python. This blog post is about why.

## Some history

For the last 5+ years, I've been one of the maintainers of a combined Python + Rust package, sourmash. This is because in [sourmash v3.0](https://github.com/sourmash-bio/sourmash/releases/tag/v3.0.0), we (well, Luiz Irber) replaced the C++ layer underneath the sourmash Python library with a Rust layer. There were two primary motivating factors: first, Luiz really wanted to run sourmash in a browser, and this was going to be much easier if we used Rust underneath (ref [pyodide](https://pyodide.org/en/stable/) and [Rust and WebAssembly](https://rustwasm.github.io/book/) and [Luiz's blog post](https://blog.luizirber.org/2018/08/27/sourmash-wasm/)). And second, Luiz wanted to use Rust multithreading to do extremely large scale searches (which he eventually started doing [in 2022](https://github.com/sourmash-bio/sra_search/commit/6313bcdd58118b1f8578461baa6d2a6467df826f) - only a few dozen lines of code!!).

This put me in a somewhat weird situation, because I didn't know Rust and yet I was left as perhaps the most active maintainer of the sourmash package - other folks (in and out of the lab) were developing new functionality, but I took on most of the bug reports and releases. For much of the time, I had to just ignore the Rust code. This was especially true once Luiz graduated and left the lab. It wasn't ideal but it was hard for me to find time to really learn Rust, and so I just let it sit - luckily, the code worked great, so it didn't cause any problems.

For the first 3 and half years years after sourmash v3.0 was released, this situation continued. Then in August 2023, I took advantage of the [new plugin framework in sourmash](http://ivory.idyll.org/blog/2023-sourmash-plugins-first-effort.html) to basically copy over Luiz's large-scale search Rust codebase and wrap it into a sourmash plugin, [sourmash_plugin_branchwater](https://github.com/sourmash-bio/sourmash_plugin_branchwater/) ([first release, v0.3](releases/tag/v0.3.0)). This was largely driven by the increasing importance of the large scale search to a variety of collaborators, and our desire to customize it in various ways.

I have a lot to say about the process of developing that plugin, but the most important thing for this blog post is this: it let us (mostly me and Tessa Pierce-Ward, but also Mo Abuelanin and Olga Botvinnik) start playing with Rust in a real application that we were using regularly.

In the two years since then, Tessa and (to a lesser extent) I and others have put in a lot of effort on our various Rust codebases. It enables high-performance multithreaded analysis in various ways, and it's become one of our main development efforts as a data set sizes grow.

Why am I writing this blog post? Because I _finally_ took a deep dive into a biggish pile of Rust code, and achieved some level of actual Rust understanding, and ... I really, really like it! And I'm really excited that [my first big PR adding real new functionality](https://github.com/sourmash-bio/sourmash_plugin_branchwater/pull/430) has been merged and is being released!

## The top reasons I love Rust

### Simple, robust multithreading is really easy.

We're using [rayon](https://crates.io/crates/rayon), and it's been pretty much as simple as saying "hey, Rust, do this iteration in parallel". If your code is threadsafe, it'll just compile and become multithreaded; if it doesn't compile, it's because your code is legitimately not threadsafe and you need to fix it ;).

### It's straightforward to track and manage object modifications, references, and lifetime

Rust has a really, really nice way of managing [variable mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html) and [references](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html).  This eases one of my main challenges in refactoring complex code in other languages, and lets me confidently use functions with clear knowledge of whether the objects are being modified (or not), and/or copies are being made.

A closely related concept is that of copying objects so that you _can_ modify them, which is typically done using `obj.clone()`. I spent a lot of time and energy figuring out how to fix some of our internal functions to only clone big objects when they needed to be cloned (ref [sourmash#3343](https://github.com/sourmash-bio/sourmash/issues/3343)), and when Luiz reviewed that and some related code, he [salted in a conversion function](https://github.com/sourmash-bio/sourmash/pull/3348) that let me refactor a bunch of code and realize [some substantial performance improvements](https://github.com/sourmash-bio/sourmash_plugin_branchwater/pull/471). It was remarkably easy and felt truly magical.

I'm sure you can do this in other languages, and it's perhaps something that Go or some other modern language - even C++, if the proper incantations are uttered - would let you do easily. In Rust, it's built in, and the compiler guides you in the right direction when you do something that's problematic. I love it!

### The compiler messages are ridiculously useful

I've never experienced a more helpful compiler - when it fails to compile code that attempts to do something unwise, it clearly and explicitly tells me what's going on, and even offers suggestions on how to fix it.

### The Python integration is really nice

I've been using [pyo3](https://pyo3.rs/) to wrap Rust code and make it accessible to Python. (sourmash still uses FFI, which involves more coding, but since it works, we're not gonna break it just yet ;).

I have a friend that insists that everything should just be rewritten in Rust. Even if I didn't have a substantial existing codebase in Python, I think Rust is still a bit too rigid to do some of the truly exploratory work that my own scientific & coding process depends on. So I'm not going to switch over to Rust completely. But I love that I can quickly build a Rust function, compile it, and then access it via Python. It's been much more straightforward than C++.

### I really like `Option` and `Result`

Rust has a really neat approach to representing values as "something" vs "nothing", and catching errors. They rely on using enums called `Option` (which can take on values `None` or `Some(val)`) and `Result` (which takes on `Ok(val)` or `Err(val)`). I'm still not completely comfortable with them - custom errors kick my butt, in particular - but they are a really important way of managing these issues in the codebase, and I like 'em a lot.

## Increasingly, Rust lets me do my work.

I'm not sure how much is my brain adjusting to Rust in a kind of Stockholm-like syndrome and how much Rust is really just that good, but either way I'm reasonably happy and productive, so I'll take it ;).

Rust is almost certainly not for everyone. I would recommend looking into it if you're stuck in C++ hell, but the transition is not that easy. In my case I lucked out because Luiz dropped a reasonably large and functioning Rust codebase in my lap, and it worked very well, so I was incentivized to learn Rust and build on the existing Rust code.

I have been searching out negative views on Rust, and I sympathize with some of them. Maybe that will grow over time. But for me, it's a massive improvement over C++. Your mileage may vary!

--titus
