
### Weak references

[weakref — Weak references — Python 3.8.1 documentation ](https://docs.python.org/3/library/weakref.html)


```py
>>> t = (1, 2, 3, 4)
>>> type(t)
<class 'tuple'>

>>> type(3)
<class 'int'>

>>> type(['foo', 'bar', 'baz'])
<class 'list'>

>>> class Foo:
...     pass
>>> type(Foo)
<class 'type'>

>>> type(Foo())
<class '__main__.Foo'>

>>> x = Foo()
>>> x
<__main__.Foo object at 0x10e988da0>

>>> type(x)
<class '__main__.Foo'>
```

[How to delete every reference of an object in Python?](https://stackoverflow.com/questions/3013304/how-to-delete-every-reference-of-an-object-in-python)

```py
>>> Foo = undefined
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'undefined' is not defined

name 'undefined' is not defined
>>>
>>> Foo = null
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'null' is not defined

name 'null' is not defined
>>> Foo = None
>>> Foo
>>>
>>> del Foo
>>> Foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Foo' is not defined

name 'Foo' is not defined
>>>
```

[How to delete every reference of an object in Python?](https://stackoverflow.com/questions/3013304/how-to-delete-every-reference-of-an-object-in-python)

```py
>>> x = "something"
>>> b = x
>>> l =[b]
>>> l
['something']

>>> type(l)
<class 'list'>

>>> type(x)
<class 'str'>

>>> type(b)
<class 'str'>

>>> del x
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined

name 'x' is not defined
>>> b
'something'

>>> l
['something']

>>> del b
>>> l
['something']

>>> b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined

name 'b' is not defined
>>> type(l[0])
<class 'str'>
```

Do garbage collect with `gc.collect()`, string is still in `l` despite having no direct references:
```
>>> import gc
>>> gc.collect()
4403

>>> l
['something']
```

[Weak reference - Wikipedia ](https://en.wikipedia.org/wiki/Weak_reference#Python)
```py
>>> import weakref
>>> import gc
>>> class Egg:
...     def spam(self):
...         print("I'm alive!")
>>> obj = Egg()
>>> weak_obj = weakref.ref(obj)
>>> weak_obj().spam()
I'm alive!
>>> obj = "Something else"
>>> gc.collect()
1112

>>> weak_obj().spam()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'spam'

'NoneType' object has no attribute 'spam'
>>> obj = Egg()
>>> obj
<__main__.Egg object at 0x10fa93d30>

>>> weak_obj().spam()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'spam'

'NoneType' object has no attribute 'spam'
>>> obj.spam()
I'm alive!
>>> obj().spam()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Egg' object is not callable

'Egg' object is not callable
>>> obj.spam()
I'm alive!
>>>
```



