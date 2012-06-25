C++ for Python Programmers: a Cheatsheet
########################################

:author: C\. Titus Brown
:tags: python, c++, msu
:date: 2009-01-07
:slug: cpp-for-python-programmers
:category: python


A fellow prof here at MSU, Rich Enbody, whipped up the following cheat-sheet
for new programmers transitioning from Python (CSE 231) to C++ (CSE 232).
He welcomes comments.  Here's the link:

    http://web.cse.msu.edu/~cse231/python2Cpp.html

Paranthetically, he and his cohort in crime, Bill Punch, will be giving a talk
about using Python as the intro CS programming language at PyCon '09.  They
have some interesting stats on the effects of a mixed Python-C++ curriculum
vs a C++-C++ course base for the first year of programming.

And folks... remember, this is for *intro* programmers who don't know
C++ yet!

--titus


----

**Legacy Comments**


Posted by Evan on 2009-01-07 at 18:59. 

::

   Pretty nice. I already know C++ pretty well but I'm going to share
   this with some of my friends who are Python-specific.


Posted by Fabien on 2009-01-07 at 19:27. 

::

   A few problems in that first draft, mostly due to the author's C
   background:      1/ In contrast to C, in C++, declaring variables at
   the beginning of the block is a bad habit at best, and quite often
   impossible.      C code:    int a, b;  a =3;  ++a;  b= 4;    C++
   equivalent:    int a= 3;  ++a;  int b= 4;        2/ "File Input and
   Output": I'm not 100% sure the code won't work, but this one is far
   better and more canonical:    int main()  {    string line;
   ifstream InStream ("Data.txt");      while (getline (InStream,line))
   {    cout &lt;&lt; line &lt;&lt; endl;  // output the line    }  }
   3/ Arrays.    C-style arrays are only used if you need to put some
   hard-coded values. And they're not even proper arrays -- they're
   nearly pointers (which pretty much means, lots of headaches).    In
   C++, the canonical type for an array is vector&lt;&gt;. It's a real
   array, whose size can change whenever you wish, and that you can copy.
   vector&lt;int&gt; a (10);  vector&lt;int&gt; b= a;  vector&lt;int&gt;
   c;  c= b;

