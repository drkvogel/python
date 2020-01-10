
[5 Python features I wish I had known earlier - Towards Data Science ](https://towardsdatascience.com/5-python-features-i-wish-i-had-known-earlier-bc16e4a13bf4)


```py
❯ ptpython
>>> aList = [1,2,3,4]
>>> a, b, c, d = aList[0:4]
>>> a, *b, c, d = aList
>>> aList
[1, 2, 3, 4]
>>> b
[2]
>>> a
1

>>> add_func = lambda z: z ** 2
>>> add_func(3)
9

>>> is_odd = lambda z: z%2 == 1
>>> is_odd(1)
True
>>> is_odd(2)
False

>>> multiply = lambda x,y:x*y
>>> multiply(2,3)
6

>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> a_list = list(range(10))
>>> a_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(a_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(list(map(add_func, a_list)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> import copy
>>> copy
<module 'copy' from '/usr/local/anaconda3/lib/python3.7/copy.py'>
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(copy)
>>> aList = copy.deepcopy(a_list)
>>> aList
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print([x ** 2 for x in aList])
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> print(list(filter(is_odd, aList)))
[1, 3, 5, 7, 9]
>>> print([x for x in aList if x%2 == 1])
[1, 3, 5, 7, 9]

>>> len(aList)
10
>>> aList[len(aList) - 2]
8
>>> aList[-2]
8
>>> aList[2:5]
[2, 3, 4]
>>> aList[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


>>> a, b, c, d = aList[0:4]
>>> print(f'a: {a}, b: {b}, c:{c}, d:{d}')
a: 0, b: 1, c:2, d:3

# unpacking
>>> a, *b, c, d = aList
>>> print(f'a: {a}, b: {b}, c:{c}, d:{d}')
a: 0, b: [1, 2, 3, 4, 5, 6, 7], c:8, d:9
>>> a
0
>>> b
[1, 2, 3, 4, 5, 6, 7]
```

```py
>>> numbers = [2, 1, 3, 4,7]
>>> more_numbers = [*numbers, 11, 18]
>>> more_numbers
[2, 1, 3, 4, 7, 11, 18]
>>> print(more_numbers)
[2, 1, 3, 4, 7, 11, 18]
>>> print(more_numbers, sep=', ')
[2, 1, 3, 4, 7, 11, 18]
>>> print(*more_numbers, sep=', ')
2, 1, 3, 4, 7, 11, 18
```

[Unpack a list in Python?](https://stackoverflow.com/questions/3480184/unpack-a-list-in-python)
[Asterisks in Python: what they are and how to use them - Trey Hunner ](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/)
[Understanding the asterisk(*) of Python - Understanding the Python - Medium ](https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558)
