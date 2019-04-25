
[magmax/python-inquirer: A collection of common interactive command line user interfaces, based on Inquirer.js ](https://github.com/SBoudrias/Inquirer.js/) (https://github.com/magmax/python-inquirer)

[Phone number validation doesn't really work correctly · Issue #25 · magmax/python-inquirer ](https://github.com/magmax/python-inquirer/issues/25)
[#25 fix phone pattern · magmax/python-inquirer@ac5104d ](https://github.com/magmax/python-inquirer/commit/ac5104d3f7e2c4e4336b57567811020fe7f859c4)

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

so but:

```
>>> re.match('asdf', 'asdf') is not None
True
>>> re.match('.*', 'asdf') is not None
True
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
