
### pip install for Python2

In VSCode, tried to rename a symbol, got:

>Rename failed to compute edits
>Refactoring library rope is not installed. Install?

Chose "Yes", then got:
>There is no Pip installer available in the selected environment.

```
2021-04-07 08:23:52 kvogel-elitebook:~/projects/primrose/kilo ±(feature/KILO-57-pick-status) ✗ 
❯ which pip
pip not found

❯ which pip3
/usr/bin/pip3

❯ which python
/usr/bin/python

❯ python -V   
Python 2.7.18

❯ which pip2
pip2 not found

❯ which pip3
/usr/bin/pip3

❯ which pip
pip not found

❯ sudo apt install python-pip
E: Unable to locate package python-pip
```

[ubuntu - How to install pip for Python 2](https://stackoverflow.com/questions/21305524/how-to-install-pip-for-python-2)
>To install pip for Python2 on Ubuntu, this worked for me:
```
sudo apt update
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
```
>It's based on DareDevil7's answer but notice the url is different.

```
2021-04-07 09:37:27 kvogel-elitebook:~/p/primrose/kilo ±(feature/KILO-57-pick-status) ✗
❯ sudo apt update

❯ curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py

❯ sudo python2 get-pip.py
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Collecting pip<21.0
  Downloading pip-20.3.4-py2.py3-none-any.whl (1.5 MB)
Collecting setuptools<45
  Downloading setuptools-44.1.1-py2.py3-none-any.whl (583 kB)
Collecting wheel
  Downloading wheel-0.36.2-py2.py3-none-any.whl (35 kB)
Installing collected packages: pip, setuptools, wheel
Successfully installed pip-20.3.4 setuptools-44.1.1 wheel-0.36.2

❯ which pip
/usr/local/bin/pip

❯ pip -V
pip 20.3.4 from /usr/local/lib/python2.7/dist-packages/pip (python 2.7)
```


Tried renaming again:

```
2021-04-07 09:49:59 kvogel-elitebook:~/projects/primrose/kilo ±(feature/KILO-57-pick-status) ✗ 
❯ /usr/bin/python /home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/pyvsc-run-isolated.py pip install -U rope --user
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Collecting rope
  Downloading rope-0.18.0.tar.gz (249 kB)
     |████████████████████████████████| 249 kB 5.5 MB/s 
Building wheels for collected packages: rope
  Building wheel for rope (setup.py) ... done
  Created wheel for rope: filename=rope-0.18.0-py2-none-any.whl size=181129 sha256=024b3ba44b9525c0838e4e1c8e3f4a758ef984345d0ef9ffc92a65d2dd5c037b
  Stored in directory: /home/kvogel/.cache/pip/wheels/55/de/de/56b2cc6e5080d13cd8a79b2d53950d13bd5edc8b3a7b5d5baf
Successfully built rope
Installing collected packages: rope
Successfully installed rope-0.18.0
```


```
Refactor failed. Syntax error in file <kilo/cservice/order/stages.py> line <527>: invalid syntax [('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 380, 'watch', 'self._process_request(self._input.readline())'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 350, '_process_request', 'int(request["indent_size"]),'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 259, '_rename', 'refactor.refactor()'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 128, 'refactor', 'self.onRefactor()'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 156, 'onRefactor', 'changes = renamed.get_changes(self._newName, task_handle=self._handle)'), ('/home/kvogel/.local/lib/python2.7/site-packages/rope/refactor/rename.py', 97, 'get_changes', 'new_co...
```
There was a syntax error... fixed it, then:
```
Refactor failed. Syntax error in file <doc/developer/code/khaos-autocode.py> line <3958>: invalid syntax [('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 380, 'watch', 'self._process_request(self._input.readline())'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 350, '_process_request', 'int(request["indent_size"]),'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 259, '_rename', 'refactor.refactor()'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 128, 'refactor', 'self.onRefactor()'), ('/home/kvogel/.vscode-server/extensions/ms-python.python-2021.3.680753044/pythonFiles/refactor.py', 156, 'onRefactor', 'changes = renamed.get_changes(self._newName, task_handle=self._handle)'), ('/home/kvogel/.local/lib/python2.7/site-packages/rope/refactor/rename.py', 97, 'get_changes',
```
OK...
```py
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False, default=Sequence('id_identity', start=1, increment=1, metadata=MetaData(bind=Engine(mssql+pyodbc://Reporting:readonly@_KHAOSHOST_REMOVED_/KHAOS_TESTING?TDS_Version=7.2&driver=FreeTDS))))
```
should be:
```py
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False, default=Sequence('id_identity', start=1, increment=1, metadata=MetaData(bind=Engine('mssql+pyodbc://Reporting:readonly@_KHAOSHOST_REMOVED_/KHAOS_TESTING?TDS_Version=7.2&driver=FreeTDS'))))
```
fixed, then...
```
Refactor failed. Syntax error in file <doc/developer/code/khaos-autocode.py> line <5565>: invalid syntax
```
load of errors the same in that file, fixed, then could rename

`join_picklist_table` -> `join_picklist`


