

```bash
(venv) [  6:16pm ]  [ kvogel@kvogel-macbook-2018:~/Projects/python/builtin(master✔) ]
 $ ipython
/usr/local/anaconda3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:763: UserWarning: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37)
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: import sys
In [2]: a = sys.builtin_module_names
In [3]: print(a)
('_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype', 'zipimport')
```

is `urllib` built in? 

```bash
 $ python3 -c "import sys; print('Count built-in modules: %d' %len(sys.builtin_module_names)); print(sys.builtin_module_names)"
Count built-in modules: 30
('_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype', 'zipimport')
```

