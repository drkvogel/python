

[properties - How does the @property decorator work in Python?](https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python)
>Documentation says it's just a *shortcut for creating readonly properties*. So
```py
@property
def x(self):
    return self._x
```
>is equivalent to
```py
def getx(self):
    return self._x
x = property(getx)
```


[python - What does Django's @property do?](https://stackoverflow.com/questions/58558989/what-does-djangos-property-do)
>It is something from Python; it is not Django-specific 
>There is nothing Django-specific on it, this is a decorator in Python

>What the `@property` decorator does, is declare that it can be accessed like it's a regular property.
>This means you can call full_name as if it were a member variable instead of a function:
```py
name = person.full_name
```
>instead of
```py
name = person.full_name()
```

>In Python we don't really have private attributes, and we want simple syntax. So we flip it: programmers often directly access an object's attributes. But what if you want to change the internal behaviour? We don't want to change the class' interface.

>@property lets you change how bar works internally without changing the external interface. Users of the class can still access foo.bar, but your internal logic can be completely different:

[Built-in Functions — Python 3.9.4 documentation ](https://docs.python.org/3/library/functions.html#property)
[How do Python properties work?](https://stackoverflow.com/questions/6193556/how-do-python-properties-work)

[The @property Decorator in Python: Its Use Cases, Advantages, and Syntax ](https://www.freecodecamp.org/news/python-property-decorator/)
[Getter and Setter in Python - GeeksforGeeks ](https://www.geeksforgeeks.org/getter-and-setter-in-python/)
[Python property decorator - Python @property - JournalDev ](https://www.journaldev.com/14893/python-property-decorator)
[decorator - Why does @foo.setter in Python not work for me?](https://stackoverflow.com/questions/598077/why-does-foo-setter-in-python-not-work-for-me)
[python - What's the pythonic way to use getters and setters?](https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters)


[The @property Decorator in Python: Its Use Cases, Advantages, and Syntax ](https://www.freecodecamp.org/news/python-property-decorator/)

[python - What does Django's @property do?](https://stackoverflow.com/questions/58558989/what-does-djangos-property-do)
>It is something from Python; it is not Django-specific

>Properties can be considered the "Pythonic" way of working with attributes because:
>* The syntax used to define properties is very *concise and readable*.
>* You can access *instance attributes* exactly as if they were *public attributes* while using the "magic" of *intermediaries (getters and setters)* to *validate* new values and to *avoid accessing or modifying the data directly*.
>* By using `@property`, you can *reuse the name* of a property to avoid creating new names for the getters, setters, and deleters.
  ?

>*A decorator function is basically a function that adds new functionality to a function that is passed as argument*. It lets us *add new functionality* to an existing function *without modifying it*.

[The @property Decorator in Python: Its Use Cases, Advantages, and Syntax ](https://www.freecodecamp.org/news/python-property-decorator/)

>`@property` is a built-in decorator for the `property()` function in Python. It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.

add getters and setters "behind the scenes" without affecting the syntax that you used to access or modify the attribute when it was public.


```py
>>> class House:
...   def __init__(self, price):
...     self._price = price
...   @property
...   def price(self):
...     return self._price
...   @price.setter
...   def price(self, new_price):
...     if new_price > 0 and isinstance(new_price, float):
...       self._price = new_price
...     else:
...       print("Please enter a valid price")
...   @price.deleter
...   def price(self):
...     del self._price
...
>>> house = House('abcd')
>>> house.price
'abcd' # setter should check `isinstance`!
>>> del house.price
>>> house.price
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in price
AttributeError: 'House' object has no attribute '_price'
>>> house.price = 50000
Please enter a valid price
>>> house.price = 50000.0
>>> house.price
50000.0
```






