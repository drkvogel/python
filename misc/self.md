

```py
>>> class MyClass:
...   def func1():
...     self.a = 1
...   def print_a():
...     print(self.a)
... 
>>> i = MyClass()
>>> i.print_a()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_a() takes 0 positional arguments but 1 was given
```
