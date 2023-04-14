
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

Wed 2022-03-02 07:59 / 14:59 ICT
reinstalled:
```
2022-03-02 07:54:48 kvogel@kvogel-surface-ubuntu:~/Downloads
❯ bp
Traceback (most recent call last):
  File "/home/kvogel/.local/bin/bpython", line 5, in <module>
    from bpython.curtsies import main
ModuleNotFoundError: No module named 'bpython'

❯ pip install bpython
...
Successfully built curtsies
Installing collected packages: urllib3, idna, cwcwidth, charset-normalizer, certifi, blessings, typing-extensions, requests, pyxdg, greenlet, curtsies, bpython
Successfully installed blessings-1.7 bpython-0.22.1 certifi-2021.10.8 charset-normalizer-2.0.12 curtsies-0.3.10 cwcwidth-0.1.6 greenlet-1.1.2 idna-3.3 pyxdg-0.27 requests-2.27.1 typing-extensions-4.1.1 urllib3-1.26.8
WARNING: You are using pip version 21.2.4; however, version 22.0.3 is available.
You should consider upgrading via the '/home/kvogel/.asdf/installs/python/3.10.2/bin/python3.10 -m pip install --upgrade pip' command.
```
>bpython-curtsies is bpython with native terminal scrolling
?

### bpython slow

bpython is now hella slow....
installed IPython

```
23/03/14 13:01:47 kvogel@kvogel-macbook-2021:~
❯ bp
bpython version 0.23 on top of Python 3.11.0 /Users/kvogel/.asdf/installs/python/3.11.0/bin/python3.11
>>> import pprint
>>> nums -
KeyboardInterrupt
>>> nums = {4:1, 3:2, 1:1, 2:3}
>>> pprint.pprint(nums, sort_dicts=True)
{1: 1, 2: 3, 3: 2, 4: 1}
>>>

23/03/14 13:03:50 kvogel@kvogel-macbook-2021:~
❯ ipython
Python 3.11.0 (main, Nov 14 2022, 13:44:00) [Clang 14.0.0 (clang-1400.0.29.202)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.11.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pprint

In [2]: nums = {4:1, 3:2, 1:1, 2:3}

In [3]: pprint.pprint(nums, sort_dicts=True)
{1: 1, 2: 3, 3: 2, 4: 1}

In [4]:
```
ptpython even better?
```
23/03/14 13:46:46 kvogel@kvogel-macbook-2021:~
❯ pip install ptpython
...
Reshimming asdf python...
❯ ptpython
>>> import pprint
>>> nums = {4:1, 3:2, 1:1, 2:3}
>>> pprint.pprint(nums, sort_dicts=True)
{1: 1, 2: 3, 3: 2, 4: 1}
>>>
```
