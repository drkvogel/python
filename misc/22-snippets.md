
[22 Python Code Snippets for Everyday Problems  by Abhay Parashar  Apr, 2021  Level Up Coding ](https://levelup.gitconnected.com/22-python-code-snippets-for-everyday-problems-4c6a216c33ae)

```
2021-04-12 13:35:25 kvogel-elitebook:~/pl/python/misc ±(master) ✗ 
❯ bpython
bpython version 0.18 on top of Python 3.8.5 /usr/bin/python3
```
```py
>>> input()
aasdf
'aasdf'
```

```py
>>> input().split()
a b c
['a', 'b', 'c']
>>> map(int, input().split())
a b c
<map object at 0x7f87503b5940>
>>> m = map(int, input().split())
a b c
>>> m
<map object at 0x7f87503b5b20>
>>> m = map(int, input().split())
1 2 3
>>> m
<map object at 0x7f87503a2b50>
>>> m[0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    m[0]
TypeError: 'map' object is not subscriptable
>>> a, b = map(int, input().split())
1 2 3
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a, b = map(int, input().split())
ValueError: too many values to unpack (expected 2)
```

