nsjwt
=====

.. image:: https://secure.travis-ci.org/cordalace/nsjwt.svg?branch=master
   :target: http://travis-ci.org/cordalace/nsjwt?branch=master

No Shit JWT implementation

Advantages:

- Damn simple: only HMAC SHA-256 ("HS256") algorithm implemented so no header parameter needed
- Fast: uses ultrajson_ and pybase64_
- No Object-Oriented shit


.. _ultrajson: https://github.com/esnme/ultrajson
.. _pybase64: https://github.com/mayeut/pybase64

Installation
------------

.. code:: sh

    pip install nsjwt

Usage
-----

.. code:: python

    >>> import nsjwt
    >>> secret = 'secret'
    >>> payload = {"sub": "1234567890", "name": "Robbie Basho", "admin": True}

    >>> nsjwt.encode(secret, payload)
    b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlJvYmJpZSBCYXNobyIsImFkbWluIjp0cnVlfQ.MvN07jU4TCXH-lrYE2qsiY5cmxHO7ZCH8eLn6WpbWFM'

    >>> nsjwt.decode(secret, b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRmFoZXkiLCJhZG1pbiI6dHJ1ZX0.XDADzzjyGLeoLBl2BHJaytkLtGdhBb5KWsKOtZlVEo8')
    {'admin': True, 'name': 'John Fahey', 'sub': '1234567890'}

License
-------

Apache 2.0 - See `the LICENSE`_ for more information.

.. _the LICENSE: https://github.com/cordalace/nsjwt/blob/master/LICENSE
