FLTK on Windows, and using 'CMake'
##################################

:author: C\. Titus Brown
:tags: python,programming
:date: 2007-01-22
:slug: using-cmake
:category: python


I spent part of the last few days figuring out how to get my
cross-platform GUI, FamilyRelations II (a.k.a. FRII), to build on
Windows.  It used to compile on my old desktop machine, which we
then converted over to MythTV with a Windows partition for compilation,
but that hard drive died during my thesis struggle.  The trick was
(and is) to get the software built with the proper combination of
libraries/library dependencies so that in the end the linking will work.

The big struggle this time turned out to be `FLTK
<http://www.fltk.org/>`__. FLTK is the cross-platform GUI system I
use; it's a fast, light ("FL") toolkit for windowing, and it works
very nicely on OS X, Windows, and Linux/X11.  I could compile it just
fine, but it turned out to be compiling with the 'mingw' compiler
instead of the standard cygwin gcc compiler, and this meant that I
couldn't link it with the *rest* of the stuff I was compiling -- in
particular, the `Xerces-C XML parser
<http://xml.apache.org/xerces-c>`__.  In the end I had to go hack on
FLTK post-configure/pre-compile, which was ... fun.

The bright spot in all of this mess was that I converted my entire C++
source tree -- 24k lines of C++ code -- over to using `CMake
<http://www.cmake.org>`__.  CMake is a build configuration system that
I hadn't noticed before last month, but it's actually used fairly
widely; the KDE project uses it, as do VTK and ITK.  A local developer
working with my code (hi Diane!) had actually spent some time
converting a subdirectory over to use cmake, too.

CMake is a complete replacement for configure, as far as I can tell.
I don't know if it covers the weird corner cases in less-used OSes,
but it seems to work pretty well for my simple need to build
binaries on Linux, OS X, and Windows.

The configuration and make steps are now as simple as this: ::

  cmake .
  make

Here, CMake configures the entire source tree, locating libraries &
other dependencies, and then creates makefiles suitable for 'make'.
(It can also create Visual Studio build files; so far no indication of
XCode/ProjectWhatever stuff for OS X.)

Most impressively, the configuration files I need to write are
actually quite small and easy to write, with essentially no
boilerplate; I converted the entire source tree over to CMake in about
an hour.  Your standard {{{CMakeLists.txt}}} file (ugly name!) looks
something like this: ::

  Project(hello)

  include_directories(./include)
  link_directories(./lib)
  link_libraries(mylib)

  add_executable(hello hello1.cc hello2.cc)

This will generate essentially this command line on Linux: ::

  gcc -I./include -L./lib -lmylib -o hello hello1.cc hello2.cc

(simplified for dramatic purposes).

If there's one frustration I have with CMake, it's that the documentation
is not well rounded.  It took me forever to find the correct incantation
to add '-mwindows' to all builds on windows: ::

   if(WIN32)
      set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mwindows")
   endif(WIN32)

Mind you, it's pretty terse & to the point when you *do* figure out how
to do things, but getting there can require a lot of grepping.

Now for the somewhat odd bit: I actually met a (the?) maintainer of
CMake, Andy, at a recent image analysis conference, the NA-MIC AHM in
Utah.  We were there to talk with `Kitware
<http://www.kitware.com/>`__ about some image analysis software
development, and it turns out that they maintain CMake and use it in a
lot of their software.  Since my local friend had been pushing it on
me already, I tried it out while at the conference and found it to be
pretty easy to use, and that spurred the rest of my conversion.

It seems odd to have met these people in person before corresponding,
when there are so many developers with whom I correspond but have
never met!

Anyway, if you're looking for a replacement for 'configure', check out
CMake.  I really like it so far.

--titus
