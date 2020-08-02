[metaclass](https://www.google.com/search?q=metaclass&ie=UTF-8)
[Python Metaclasses – Real Python ](https://realpython.com/python-metaclasses/)
[oop - What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
[oop - What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python/100037#100037)

A metaclass is the class of a class. 
A class defines how an instance of the class (i.e. an object) behaves while a metaclass defines how a class behaves. 
A class is an instance of a metaclass.

type is the usual metaclass in Python. type is itself a class, and it is its own type. You won't be able to recreate something like type purely in Python, but Python cheats a little. To create your own metaclass in Python you really just want to subclass type.

### `object` pre-defined variable

```py
>>> object
<class 'object'>
>>> type(object)
<class 'type'>
```
???

[class Classname(object), what sort of word is 'object' in Python?](https://stackoverflow.com/questions/10044321/class-classnameobject-what-sort-of-word-is-object-in-python)
[Python class inherits object](https://stackoverflow.com/questions/4015417/python-class-inherits-object)


object is a (global) variable. By default it is bound to a built-in class which is the root of the type hierarchy.