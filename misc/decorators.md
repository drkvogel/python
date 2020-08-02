
[Demystifying Python Decorators  Level Up Coding ](https://levelup.gitconnected.com/demystifying-python-decorators-726f04963a52)
[Python decorators just syntactic sugar?](https://stackoverflow.com/questions/12295974/python-decorators-just-syntactic-sugar)
>the decorator syntax is syntactic sugar because writing `@decorator` above the function definition is the same as calling `f = decorator(f)` after it.

[The @property Decorator in Python: Its Use Cases, Advantages, and Syntax ](https://www.freecodecamp.org/news/python-property-decorator/)

*A decorator function is basically a function that adds new functionality to a function that is passed as argument*.
It lets us *add new functionality* to an existing function *without modifying it*.

```py
>>> def initial_function():
...   print("Initial functionality")
...
>>> initial_function()
Initial functionality
>>> def decorator(f):
...   def new_function():
...     print("Extra functionality")
...     f()
...   return new_function
...
>>> @decorator
... def initial_function():
...   print("Initial functionality")
...
>>> initial_function()
Extra functionality
Initial functionality
```
