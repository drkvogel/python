
### python-inguirer

[magmax/python-inquirer: A collection of common interactive command line user interfaces, based on Inquirer.js ](https://github.com/SBoudrias/Inquirer.js/) (https://github.com/magmax/python-inquirer)

>The function used for validate must take two arguments; the first is a dictionary with previously given answers, and the second is the current answer.

#### phone number won't validate in example code

[Phone number validation doesn't really work correctly · Issue #25 · magmax/python-inquirer ](https://github.com/magmax/python-inquirer/issues/25)
[#25 fix phone pattern · magmax/python-inquirer@ac5104d ](https://github.com/magmax/python-inquirer/commit/ac5104d3f7e2c4e4336b57567811020fe7f859c4)

test with:
```
2019-04-25 14:04:24 kvogel@kvogel-lubuntu ~/Projects/python/cmdline
$ ./inquirer_test.py 
```

doesn't work on Linux (kvogel-lubuntu) either

>Python automatically stores the value of the last expression in the interpreter to a particular variable called "_

`re.match() `and `re.search()` return a `MatchObject` or `None` if no match is found
docs say a `MatchObject` is truthy, but:

```py
>>> True == re.match('asdf', 'asdf')
False
>>> True == re.search('asdf', 'asdf')
False
```

but:

```
>>> re.match('asdf', 'asdf') is not None
True
>>> re.match('.*', 'asdf') is not None
True
```

Just because something is truthy doesn't mean it equals `True`!:

```py
>>> mylist = []
>>> len(mylist)
0
>>> True == len(mylist)
False                           # as expected, an empty list is falsy
>>> False == len(mylist)
True                            # as expected, an empty list is falsy (and also False?)
>>> mylist = [1,2,3]            # an non-empty list is truthy
>>> False == len(mylist)
False                           # as expected
>>> True == len(mylist)   
False                           # but it is not *equal* to True!
>>> True == bool(len(mylist))
True                            # unless you cast to bool
```

red herring, the args were the wrong way round:

So the one that works is:
```python
validate=lambda x, _: re.match('\+?\d[\d ]+\d', _),
```
not:
```python
validate=lambda _, x: re.match('\+?\d[\d ]+\d', x)
```
from the example. Note that  `_` and `x` are swapped in the arguments to the lambda and the second argument to `re.match()` is `_`, not `x`.
