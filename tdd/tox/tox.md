
### tox

tox is a generic virtualenv management and test command line tool you can use for: checking your package installs correctly with different Python versions

[python tox](https://www.google.com/search?q=python+tox&ie=UTF-8)
[Python tox - Why You Should Use It and Tutorial ](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/)
[Testing With Tox — Python 401 2.1 documentation ](https://codefellows.github.io/sea-python-401d4/lectures/testing_with_tox.html)
[Welcome to the tox automation project — tox 3.15.2.dev3 documentation ](https://tox.readthedocs.io/en/latest/)

automation of tedious Python related test activities:
test your Python package against many interpreter and dependency configs
automatic customizable (re)creation of virtualenv test environments
installs your setup.py based project into each virtual environment
test-tool agnostic: runs pytest, nose or unittests in a uniform manner

>tox is nice because it makes your testing a little more portable. *You can run tox locally and in travis (or other CI)*. It's nice to locally run tests in a virtualenv before pushing a commit and having to wait for travis to confirm.
