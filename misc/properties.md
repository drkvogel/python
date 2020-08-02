

[python decorator setter](https://www.google.com/search?q=python+decorator+setter&ie=UTF-8)
[The @property Decorator in Python: Its Use Cases, Advantages, and Syntax ](https://www.freecodecamp.org/news/python-property-decorator/)
[Getter and Setter in Python - GeeksforGeeks ](https://www.geeksforgeeks.org/getter-and-setter-in-python/)
[Python property decorator - Python @property - JournalDev ](https://www.journaldev.com/14893/python-property-decorator)
[decorator - Why does @foo.setter in Python not work for me?](https://stackoverflow.com/questions/598077/why-does-foo-setter-in-python-not-work-for-me)
[python - What's the pythonic way to use getters and setters?](https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters)


Properties can be considered the "Pythonic" way of working with attributes because:

* The syntax used to define properties is very *concise and readable*.
* You can access instance attributes exactly as if they were public attributes while using the "magic" of intermediaries (getters and setters) to *validate* new values and to *avoid accessing or modifying the data directly*.
* By using @property, you can *reuse the name* of a property to avoid creating new names for the getters, setters, and deleters.
  ?

*A decorator function is basically a function that adds new functionality to a function that is passed as argument*.
It lets us add new functionality to an existing function without modifying it.

[The @property Decorator in Python: Its Use Cases, Advantages, and Syntax ](https://www.freecodecamp.org/news/python-property-decorator/)

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






