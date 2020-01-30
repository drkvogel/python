

[cpython - How can I tell which python implementation I'm using?](https://stackoverflow.com/questions/14718135/how-can-i-tell-which-python-implementation-im-using)

```
20/01/21 2:40:54 kvogel-macbook:~/Downloads
❯ ptpython
```
```py
>>> import platform
>>> platform.python_implementation()
'CPython'
```

[python - Which setup is more efficient? Flask with pypy, or Flask with gevent?](https://stackoverflow.com/questions/14294643/which-setup-is-more-efficient-flask-with-pypy-or-flask-with-gevent)
>Both 'pypy' and 'gevent' are supposed to provide high performance. Pypy is supposedly faster than CPython, while gevent is based on co-routines and greenlets, which supposedly makes for a faster web server.

### pypy

[pypy.md](pypy.md)

### stackless

[stackless.md](stackless.md)

### greenlets

greenlets Werkzeug
[greenlet: Lightweight concurrent programming — greenlet 0.4.0 documentation ](https://greenlet.readthedocs.io/en/latest/)
> The “greenlet” package is a spin-off of Stackless, a version of CPython that supports micro-threads called “tasklets”. 

### gevent

[What is gevent? — gevent 1.5a4.dev0 documentation ](http://www.gevent.org/)
>gevent is a coroutine -based Python networking library that uses greenlet to provide a high-level synchronous API on top of the libev or libuv event loop.
