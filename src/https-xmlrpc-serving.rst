Serving XML-RPC over HTTPS with Python
######################################

:author: C\. Titus Brown
:tags: python
:date: 2008-06-17
:slug: https-xmlrpc-serving
:category: python


We've been talking about how to manage `pygr
<http://code.google.com/p/pygr>`__ resources remotely via the existing
XML-RPC interface, and for that HTTPS is a requirement.  I offered to
track down the code necessary for running an XML-RPC server over
HTTPS.  Here's what I found: ::

  It turns out that while the Python stdlib supports HTTPS client
  connections (connecting to https:// URLs), it does not directly support
  HTTPS serving.  To do that, you need to use pyOpenSSL.  However, once
  that's installed it's a breeze: it's as simple as this,

    server = SecureXMLRPCServer(server_address, KEYFILE, CERTFILE)

  You can download the SecureXMLRPCServer code and an example here:

        http://iorich.caltech.edu/~t/transfer/xmlrpc-https.tar.gz

  To run it just install pyOpenSSL ('python-openssl' under Debian),
  and then execute 'python serve-ssl.py' in one shell and 'python
  test-conn-ssl.py' in another.

Thanks to Laszlo Nagy for `his Python Cookbook recipe <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496786>`__ which only needed a bit of
fixing (for Python 2.5) and refactoring (for reusability).

The example .tar.gz above contains a private key and certification so that
the code Just Works.

--titus

p.s. Ping me at titus@idyll.org if the .tar.gz file isn't accessible and
I'll repost it.
