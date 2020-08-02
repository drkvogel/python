

[unittest introduction - Python Testing ](https://pythontesting.net/framework/unittest/unittest-introduction/)

used to be called PyUnit, due to it’s legacy as a xUnit style framework.

standard workflow is:
1. You define your own class derived from unittest.TestCase.
1.1. use `setUp` and `tearDown` functions to get your system ready for the tests.
2. Then you fill it with functions that start with ‘test_’.
3. You run the tests by placing unittest.main() in your file, usually at the bottom.


[test_um.py](test_um.py)

run directly (use `unittest`:
```
(base) 20/06/3 14:53:41 kvogel-macbook-2018:~/Projects/python/tdd/unittest ±(master) ✗ 
❯ python test_um.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
running with `-v` is more verbose, showing which tests ran
```
❯ python test_um.py -v                 
test_numbers_3_4 (__main__.TestUM) ... ok
test_strings_a_3 (__main__.TestUM) ... ok
----------------------------------------------------------------------
Ran 2 tests in 0.000s
OK
```

run with `pytest`:
```
(base) 20/06/3 14:53:54 kvogel-macbook-2018:~/Projects/python/tdd/unittest ±(master) ✗ 
❯ pytest
================================================================ test session starts ====
platform darwin -- Python 3.7.3, pytest-5.2.4, py-1.8.0, pluggy-0.12.0
rootdir: /Users/kvogel/Projects/python/tdd/unittest
plugins: astropy-header-0.1.1, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.1, cov-2.8.1
collected 2 items                                                                                                                                    
test_um.py ..                                                                                                                                  [100%]
================================================================= 2 passed in 0.31s ====
(base) 20/06/3 14:56:16 kvogel-macbook-2018:~/Projects/python/tdd/unittest ±(master) ✗ 
```

reference for all of the assert functions: [25.3. unittest — Unit testing framework — Python 2.7.18 documentation ](https://docs.python.org/2/library/unittest.html#unittest.TestCase)


Let’s say that you’ve got a bunch of test files. It would be annoying to have to run each test file separately. That’s where test discovery comes in handy.

```
(base) 20/06/3 15:03:57 kvogel-macbook-2018:~/Projects/python/tdd/unittest ±(master) ✗ 
❯ python -m unittest discover -v tests
test_numbers_5_6 (test_um.TestUM) ... ok
test_strings_b_4 (test_um.TestUM) ... ok
----------------------------------------------------------------------
Ran 2 tests in 0.001s
OK
```


>>> [x for x in l if x is not None]
[1, 2, 5, 6]

`git commit -m "hacked test to comply, bad practice but ..."`




---

Astropy. A Community Python Library for Astronomy. ?