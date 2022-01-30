
# bpython



### Running bpython inside a virtualenv

[python - Running bpython inside a virtualenv](https://stackoverflow.com/questions/25434576/running-bpython-inside-a-virtualenv)
>bpython must be installed in the virtualenv, otherwise the external, system-wide bpython is called:
>bpython has the python it was installed with hardcoded in its shebang. You can manually edit it to make it use the current python. Open the script by running for instance
>`vi $(which bpython)` Then change the top line from eg. `#!/usr/bin/python3` to eg. `#!/usr/bin/env python3`

```
(venv) 2022-01-29 06:42:52 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/flask ±(master) ✗ 
❯ vi $(which bpython)
```
```diff
-#!/usr/bin/python3
+#!/usr/bin/env python3
```
```
❯ bp                 
Traceback (most recent call last):
  File "/home/kvogel/.local/bin/bpython", line 5, in <module>
    from bpython.curtsies import main
ModuleNotFoundError: No module named 'bpython'
❯ pip install bpython
❯ bp
bpython version 0.22.1 on top of Python 3.8.10 /home/kvogel/projects/general/work/uhs/flask/venv/bin/python3
```
```py
>>> import flask
>>> 
```

Has bugs???
doesn't execute code in the same way as CPython???
search ~/p, ~/pw etc
