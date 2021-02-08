
### re-import a module

e.g. for testing changes via a REPL

reimporting a module e.g. in a REPL doesn't seem to reflect the changes made to the module
[python - What happens when a module is imported twice?](https://stackoverflow.com/questions/19077381/what-happens-when-a-module-is-imported-twice)
>A Python script will load a module only once. To reload it, use: `reload()` (Python 2) or `imp.reload()` (Python 3)

[Built-in Functions — Python 2.7.18 documentation ](https://docs.python.org/2/library/functions.html#reload)
[imp — Access the import internals — Python 3.9.1 documentation ](https://docs.python.org/3/library/imp.html)
>Deprecated since version 3.4: The imp module is deprecated in favor of importlib.

[importlib — The implementation of import — Python 3.9.1 documentation ](https://docs.python.org/3/library/importlib.html#module-importlib)
[importlib — The implementation of import — Python 3.9.1 documentation ](https://docs.python.org/3/library/importlib.html#importlib.reload)

>Instead of `from Module import function`, I should import the whole module `import Module`, then call the function by `Module.function(`). This is because `from ReloadTest import reloadtest` and `importlib.reload(ReloadTest)` *can't go together*.

```py
>>> import src.dev
>>> ts = TabSutra()
>>> ts.go()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    ts.go()
  File "/home/kvogel/projects/tabsutra/src/dev.py", line 97, in go
UnboundLocalError: local variable 'time' referenced before assignment
```
(fix problem)
```py
>>> importlib.reload(src)
<module 'src' from '/home/kvogel/projects/tabsutra/src/__init__.py'>
```
looks good, but:
```py
>>> ts.go()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    ts.go()
  File "/home/kvogel/projects/tabsutra/src/dev.py", line 97, in go
UnboundLocalError: local variable 'time' referenced before assignment
```
still there
```py
>>> importlib.reload(src.dev)
<module 'src.dev' from '/home/kvogel/projects/tabsutra/src/dev.py'>
>>> ts.go()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    ts.go()
  File "/home/kvogel/projects/tabsutra/src/dev.py", line 97, in go
UnboundLocalError: local variable 'time' referenced before assignment
```
maybe you have to import it again?
```py
>>> import src.dev
>>> ts = TabSutra()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    ts = TabSutra()
NameError: name 'TabSutra' is not defined
>>> dir(src.dev)
['Options', 'SessionNotCreatedException', 'StaleElementReferenceException', 'TabSutra', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'main', 'os', 'platform', 'sys', 'time', 'webdriver']
>>> ts = src.dev.TabSutra()
>>> 
```

```py
>>> import importlib
>>> importlib.reload(src.dev)
<module 'src.dev' from '/home/kvogel/projects/tabsutra/src/dev.py'>
```
reloaded, but not reimported yet, error still there:
```py
>>> ts.go()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    ts.go()
  File "/home/kvogel/projects/tabsutra/src/dev.py", line 99, in go
TypeError: Tuple or struct_time argument required
```
`import` again
```py
>>> import src.dev
>>> ts = src.dev.TabSutra()
>>> ts.go()
boo! # change I made - module has been reloaded and reimported
```

In fact, can put all on one line, e.g.:
```py
>>> importlib.reload(src.dev); import src.dev; ts = src.dev.TabSutra(); ts.go()
<module 'src.dev' from '/home/kvogel/projects/tabsutra/src/dev.py'>
boo asfasdfasdfasd xxx!
```
