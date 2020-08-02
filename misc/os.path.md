
```
(base) 20/05/30 14:56:52 kvogel-macbook-2018:~/Projects-work
❯ bpython
bpython version 0.18 on top of Python 3.7.3 /usr/local/anaconda3/bin/python
```
```py
>>> import os
>>> os.path
<module 'posixpath' from '/usr/local/anaconda3/lib/python3.7/posixpath.py'>
>>> os.path.curdir
'.'
>>> os.path.abspath(os.path.curdir)
'/Users/kvogel/Projects-work'
>>> os.path.expanduser(os.path.abspath(os.path.curdir))
'/Users/kvogel/Projects-work'
>>> os.path.expanduser('~')
'/Users/kvogel'
>>> os.path.expanduser('~kvogel')
'/Users/kvogel'
>>>
```

