
# doctest

TL;DNR: good for small scripts, for documenting for non-programmers e.g. scientists, and for making sure docs match code

[doctest introduction - Python Testing ](https://pythontesting.net/framework/doctest/doctest-introduction/)
[does anyone still use doctest?](https://www.google.com/search?q=does+anyone+still+use+doctest%3F&ie=UTF-8)
[Does Python doctest remove the need for unit-tests?](https://stackoverflow.com/questions/2642282/does-python-doctest-remove-the-need-for-unit-tests)


```
(base) 20/06/3 14:46:11 kvogel-macbook-2018:~/Projects/python/tdd/doctest ±(master) ✗ 
❯ python -m doctest unnecessary_math.py
**********************************************************************
File "/Users/kvogel/Projects/python/tdd/doctest/unnecessary_math.py", line 14, in unnecessary_math.multiply
Failed example:
    multiply('a', 4)
Expected:
    'aaax'
Got:
    'aaaa'
**********************************************************************
1 items had failures:
   1 of   3 in unnecessary_math.multiply
***Test Failed*** 1 failures.
```


[unit testing - Python - doctest vs. unittest](https://stackoverflow.com/questions/361675/python-doctest-vs-unittest)

>I don't use doctest as a replacement for unittest. Although they overlap a bit, the two modules don't have the same function:
>I use unittest as a unit testing framework, meaning it helps me determine quickly the impact of any modification on the rest of the code.
>I use doctest as a guarantee that comments (namely docstrings) are still relevant to current version of the code.
>The widely documented benefits of test driven development I get from unittest. doctest solves the far more subtle danger of having outdated comments misleading the maintenance of the code.

>There's a lot less boilerplate, and I find tests much simpler to write (and read). The low startup cost to write tests (ie just write a "test_foo()" function and go) also helps fight off the temptation to do the interesting code bits before nailing down your tests. 

>Another advantage of doctesting is that you get to make sure your code does what your documentation says it does. After a while, software changes can make your documentation and code do different things.

>I work as a bioinformatician, and most of the code I write is "one time, one task" scripts, code that will be run only once or twice and that execute a single specific task.

>In this situation, writing big unittests may be overkill, and doctests are an useful compromise. They are quicker to write, and since they are usually incorporated in the code, they allow to always keep an eye on how the code should behave, without having to have another file open. That's useful when writing small script.

>Also, doctests are useful when you have to pass your script to a researcher that is not expert in programming. Some people find it very difficult to understand how unittests are structured; on the other hand, doctests are simple examples of usage, so people can just copy and paste them to see how to use them.

>So, to resume my answer: doctests are useful when you have to write small scripts, and when you have to pass them or show them to researchers that are not computer scientists.