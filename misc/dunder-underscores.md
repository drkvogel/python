
### cheat sheet

Pattern	Example	Meaning
* Single Leading Underscore `_var`	Naming *convention* indicating a name is meant for *internal use*. Generally not enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.
* Single Trailing Underscore `var_`	Used by *convention* to avoid *naming conflicts* with *Python keywords*.
* Double Leading Underscore `__var`	Triggers *name mangling* when used in a *class* context. Enforced by the Python interpreter.
* Double Leading and Trailing Underscore `__var__`	Indicates *special methods* defined by the Python language. Avoid this naming scheme for your own attributes.
* Single Underscore `_`	Sometimes used as a name for temporary or insignificant variables (“don’t care”). Also: The result of the last expression in a Python REPL.


[sunder dunder](https://www.google.com/search?q=sunder+dunder&ie=UTF-8)
[Dunder or magic methods in Python - GeeksforGeeks ](https://www.geeksforgeeks.org/dunder-magic-methods-python/)
[single and double leading underscore python](https://www.google.com/search?q=single+and+double+leading+underscore+python&ie=UTF-8)
[Naming with Underscores in Python - Python Features - Medium ](https://medium.com/python-features/naming-conventions-with-underscores-in-python-791251ac7097)
[Underscores in Python ](https://shahriar.svbtle.com/underscores-in-python)

[The Meaning of Underscores in Python – dbader.org ](https://dbader.org/blog/meaning-of-underscores-in-python)


[What’s the Meaning of Single and Double Underscores In Python? | by Ahmed Besbes | Jan, 2022 | Towards Data Science ](https://towardsdatascience.com/whats-the-meaning-of-single-and-double-underscores-in-python-3d27d57d6bd1)
>1 — Single leading underscores: `_foo` - syntax hint  that these objects are used internally
>2 — Single trailing underscores: `foo_` - where you want to use a variable name that is actually a reserved keyword in Python such as `class`, def , type , object , etc.
>3 — Single underscore: `_` To define temporary or unused variables.
>4 — Double leading and trailing underscores: `__foo__` special universal class methods called dunder methods. reserved methods that you can still overwrite.
>5 — Double leading underscores: `__bar` - used for name mangling, a process by which the interpreter changes the attribute name to avoid naming collisions in subclasses.  the interpreter prepends the attribute with a single `_` plus the class name. This is done to avoid the value of the `__brand` attribute getting overridden in subclasses.

[Dunder/Magic Methods in Python | Engineering Education (EngEd) Program | Section ](https://www.section.io/engineering-education/dunder-methods-python/)


### leading underscore

>The underscore prefix is meant as a *hint* to another programmer that a variable or method starting with a single underscore is intended for internal use.

```py
>>> class Test:
...   def __init__(self):
...     self.foo = 11
...     self._bar = 23
...
>>> test = Test()
>>> test.foo
11
>>> test._bar
23
```
>leading underscores *do* impact how names get imported from modules.

>By the way, wildcard imports should be avoided (see [PEP 8: The Style Guide for Python Code ](https://pep8.org/#imports)) as they make it unclear which names are present in the namespace. It’s better to stick to regular imports for the sake of clarity.

### 2. Single Trailing Underscore: var_

a single trailing underscore (postfix) is used by *convention* to *avoid naming conflicts* with Python *keywords*.

### 3. Double Leading Underscore: __var

name mangling - to protect the variable from getting overridden in subclasses.
>A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses.

```py
>>> class ManglingTest:
...   def __init__(self):
...     self.__mangled = 'Hello'
...   def get_mangled(self):
...     return self.__mangled
...
>>> ManglingTest().get_mangled()
'Hello'
>>> ManglingTest().__mangled
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ManglingTest' object has no attribute '__mangled'
```
name mangling affects all names that start with two underscore characters (“dunders”) in a class context:

it works the other way:

```py
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled

>>> MangledGlobal().test()
23
```
The Python interpreter automatically expanded the name __mangled to _MangledGlobal__mangled because it begins with two underscore characters.


### 4. Double Leading and Trailing Underscore: __var__ (dunders)

>pronounce `__baz` as “dunder baz”. Likewise `__init__` would be pronounced as “dunder init”, even though one might think it should be “dunder init dunder.” But that’s just yet another quirk in the naming convention. It’s like a secret handshake for Python developers 🙂

These dunder methods are often referred to as *magic methods* — but many people in the Python community, including myself, [don’t like that](http://www.pixelmonkey.org/2013/04/11/python-double-under-double-wonder).

names that have both leading and trailing double underscores are reserved for special use in the language. This rule covers things like __init__ for object constructors, or __call__ to make an object callable.

name mangling is *not* applied if a name starts and ends with double underscores.

### 5. Single Underscore: _

a single standalone underscore is sometimes used as a name to indicate that a variable is temporary or insignificant.
a “don’t care” variable to ignore particular values.
this meaning is “per convention” only and there’s no special behavior triggered in the Python interpreter. The single underscore is simply a valid variable name that’s sometimes used for this purpose.

```py
>>> for _ in range(32):
...     print('Hello, World.')
```

```py
>>> car = ('red', 'auto', 12, 3812.4)
>>> color, _, _, mileage = car
>>> color
'red'
>>> mileage
3812.4
>>> _
12
```

*BUT* -  `_` *is* a special variable in most Python *REPLs* that represents the *result of the last expression* evaluated by the interpreter.

