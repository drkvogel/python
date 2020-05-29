
[Use id() to Understand 6 Key Concepts in Python - Better Programming - Medium ](https://medium.com/better-programming/use-id-to-understand-6-key-concepts-in-python-73e0bbd461ec)
[Built-in Functions — Python 3.8.3 documentation ](https://docs.python.org/3/library/functions.html#id)


```py
>>> list0 = [1, 2,3,4]
>>> list1 = [1,2,3,4]
>>> list0 == list1 # True
>>> list0 is list1 # False
>>> id(list0) # 4547685704
>>> id(list1) # 4548395912
>>> id(list0) == id(list1) # False
>>> str0 = 'Hello'
>>> str1 = str0
>>> str0 == str1 # True
>>> str0 is str1 # True
>>> id(str0) # 4548385008
>>> id(str1) # 4548385008
>>>
```
