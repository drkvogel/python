
any way to import a module from a different directory?
```
21/02/8 19:33:34 kvogel-elitebook:~/projects/tabsutra ±(master) ✗ 
❯ bpython
bpython version 0.18 on top of Python 3.8.5 /usr/bin/python3
```
```py
>>> from src.dev import TabSutra
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    from src.dev import TabSutra
ModuleNotFoundError: No module named 'src'
>>> from .src.dev import TabSutra
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    from .src.dev import TabSutra
ImportError: attempted relative import with no known parent package
>>>
```

[python - Importing files from different folder](https://stackoverflow.com/questions/4383571/importing-files-from-different-folder)
>Nothing wrong with: `from application.app.folder.file import func_name`. Just make sure folder also contains an `__init__.py`, this allows it to be included as a package. Not sure why the other answers talk about `PYTHONPATH`.

```
21/02/8 19:40:14 kvogel-elitebook:~/projects/tabsutra ±(master) ✗ 
❯ touch src/__init__.py
❯ bpython
bpython version 0.18 on top of Python 3.8.5 /usr/bin/python3
```
```py
>>> from src.dev import TabSutra
>>> ts = TabSutra()
>>> ts.get_platform()
platform.system(): Linux
'wsl'
```
or if you import the whole module you can [reload it](/blog/210208-reimport-module.md):
```py
>>> import src.dev; ts = src.dev.TabSutra() ts.go()
...
```
change something in `src.dev`, then:
```py
>>> importlib.reload(src.dev); import src.dev; ts = src.dev.TabSutra(); ts.go()
module was changed!
```
