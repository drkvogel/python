
[python - How do I install pip on macOS or OS X?](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)
[make python3 default mac](https://www.google.com/search?q=make+python3+default+mac&ie=UTF-8)
[How to set Python's default version to 3.x on OS X?](https://stackoverflow.com/questions/18425379/how-to-set-pythons-default-version-to-3-x-on-os-x)
[The right and wrong way to set up Python 3 on MacOS  Opensource.com ](https://opensource.com/article/19/5/python-3-default-mac)
[xkcd: Python Environment ](https://xkcd.com/1987/)
just use python3 and pip3 for one-off programs, and virtualenv otherwise

[10 Cool Python Project Ideas for Python Developers  by Claire D. Costa  Sep, 2020  Towards Data Science ](https://towardsdatascience.com/10-cool-python-project-ideas-for-python-developers-7953047e203)

```
2020-02-18 23:52:17 user@users-MBP ~
$ pip3 install ptpython
Collecting ptpython
...
2020-02-18 23:52:31 user@users-MBP ~
$ ptpython
```

```py
>>> import sys
>>> sys.version
'3.7.0 (default, Aug 22 2018, 15:22:33) \n[Clang 9.1.0 (clang-902.0.39.2)]'

>>> from datetime import date
>>> user = 'eric_idle'
>>> member_since = date(1975, 7, 31)
>>> f'{user} {member_since}'
'eric_idle 1975-07-31'

>>> def parse(family):
...     lastname, *members = family.split()
...     return (lastname.upper(), *members)
>>> parse('simpsons homer marge bart lisa sally')
('SIMPSONS', 'homer', 'marge', 'bart', 'lisa', 'sally')
```

```
❯ bpython
bpython version 0.18 on top of Python 3.7.3 /usr/local/anaconda3/bin/python
```
```py
>>> from statistics import mean
>>> mean([1.959, 1.205, 1.198, 1.198, 1.175, 1.169])
1.3173333333333335
>>> mean([0.892, 0.877, 0.864, 0.893, 0.865, 0.889])
0.88
>>> 1.31733 - 0.88
0.4373299999999999
```

2020-05-29 14:50:03
python testing [python/tdd/testing.md](file:///Users/kvogel/Projects/python/tdd/testing.md)
  TL;DNR: use `unittest` for this tech test, and `pytest` IRL



[Episode #28: Using Pylance to Write Better Python Inside of Visual Studio Code – The Real Python Podcast ](https://realpython.com/podcasts/rpp/28/?utm_campaign=2020-09-25)

[A Pythonic Guide to SOLID Design Principles - DEV Community 👩‍💻👨‍💻 ](https://dev.to/ezzy1337/a-pythonic-guide-to-solid-design-principles-4c8i)

[Learn Pytest in 60 Minutes : Python Unit Testing Framework](https://www.youtube.com/watch?v=bbp_849-RZ4)

that really good Python site: [PyCoder’s Weekly](https://pycoders.com/issues/430)


[Andrew Burrows - Testing the untestable: a beginner’s guide to mock objects](https://www.youtube.com/watch?v=jsjParCB7BU)
[Mocking Strategies in Python](https://www.youtube.com/watch?v=zW0f4ZRYF5M)
[Intro to Python Mocks](https://www.youtube.com/watch?v=smPbDqGjFAI)

[Python for Beginners — Object-Oriented Programming  by Siva Ganesh Kantamani  Better Programming  Jul, 2020  Medium ](https://medium.com/better-programming/python-for-beginners-object-oriented-programming-3b231bb3dd49)


[8 Advanced Python Tricks Used by Seasoned Programmers ](https://towardsdatascience.com/8-advanced-python-tricks-used-by-seasoned-programmers-757804975802)

[__slots__](/misc/__slots__.md)

[Why Does Python Recommend the Snake-Case Nomenclature?  Pawan Jain in Towards Data Science - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/#inbox/FMfcgxwJXBzMGmDLXHdQQdBlnCnkfDnD)

[Become a Python “One-Liners” Specialist  by Radian Krisno  Jun, 2020  Towards Data Science ](https://towardsdatascience.com/become-a-python-one-liners-specialist-8c8599d6f9c5)

[Python Job Board – Python Jobs HQ ](https://www.pythonjobshq.com/?__s=5r8stehqp1fcvezhd5ng)
[Grow Your Python Portfolio With 13 Intermediate Project Ideas – Real Python ](https://realpython.com/courses/intermediate-project-ideas/)


[Monty Python: The Lost World of Roiurama / Six More Minutes of Monty Python's Flying Circus](http://www.montypython.net/scripts/lostworld.php)
[Monty Python - The Lost World of Roiurama - video dailymotion ](https://www.dailymotion.com/video/x2rpx6n)

[Our Success Stories  Python.org ](https://www.python.org/success-stories/)

### CPython source code

[Python Release Python 3.7.1  Python.org ](https://www.python.org/downloads/release/python-371/)
[Python Release Python 3.8.6  Python.org ](https://www.python.org/downloads/release/python-386/)
```
20/10/5 14:47:46 kvogel-macbook-2018:~/Downloads
❯ file Python-3.8.6-src.tgz
Python-3.8.6-src.tgz: gzip compressed data, last modified: Wed Sep 23 13:54:28 2020, max compression, from Unix, original size 87797760
❯ tar tzf Python-3.8.6-src.tgz| less
❯ tar xzf Python-3.8.6-src.tgz
(venv) 20/10/5 14:51:10 kvogel-macbook:~/Projects/python/ ±(master) ✗ 
❯ mv ~/Downloads/Python-3.8.6/ src
```

[PEP 3101 -- Advanced String Formatting  Python.org ](https://www.python.org/dev/peps/pep-3101/)
`!r` - convert the value to a string using repr().
`!s` - convert the value to a string using str().

[str() vs repr() in Python - GeeksforGeeks ](https://www.geeksforgeeks.org/str-vs-repr-in-python/)
>`str()` is used for creating output for end user while `repr()` is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable. 

[New tutorials from Flavio! - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/#inbox/FMfcgxwKkbrQKfNknVffDdqgbHxJwlSF)
[Python Introspection Tutorial ](https://flaviocopes.com/python-introspection/)
[Python Annotations Tutorial ](https://flaviocopes.com/python-annotations/)
[Python, how to list files and folders in a directory ](https://flaviocopes.com/python-list-files-folders/)
[Python, how to check if a number is odd or even ](https://flaviocopes.com/python-number-odd-even/)
[Python, how to get the details of a file ](https://flaviocopes.com/python-get-file-details/)
[Python, how to check if a file or directory exists ](https://flaviocopes.com/python-check-file-exists/)
[Python Exceptions Tutorial ](https://flaviocopes.com/python-exceptions/)

[Speed Up Python With Concurrency – Real Python ](https://realpython.com/courses/speed-python-concurrency/?utm_campaign=2020-12-08)

[pypy](https://www.google.com/search?q=pypy&ie=UTF-8)
[python 3.x - what's the differences python3 and pypy3](https://stackoverflow.com/questions/59050724/whats-the-differences-python3-and-pypy3)
[RPython](https://www.google.com/search?q=RPython&ie=UTF-8)
[Stackless Python - Wikipedia ](https://en.wikipedia.org/wiki/Stackless_Python)
[python - Why shouldn't I use PyPy over CPython if PyPy is 6.3 times faster?](https://stackoverflow.com/questions/18946662/why-shouldnt-i-use-pypy-over-cpython-if-pypy-is-6-3-times-faster)
[pypy C benchmark cPickle, cStringIO cpython](https://www.google.com/search?q=pypy++C+benchmark+cPickle%2C+cStringIO+cpython&gs_lcp=CgZwc3ktYWIQAzoECAAQR1DROFjRjgFgqJABaAFwAngAgAG4AYgBrQ-SAQQyMi4ymAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&uact=5)
[RustPython/RustPython: A Python Interpreter written in Rust ](https://github.com/RustPython/RustPython)

[pydantic ](https://pydantic-docs.helpmanual.io/)

mockist tdd, microservices...
[Testing the untestable: a beginner’s guide to mock objects](https://www.youtube.com/watch?v=jsjParCB7BU)
[Mocking Strategies in Python](https://www.youtube.com/watch?v=zW0f4ZRYF5M)
[Why Isn't Functional Programming the Norm? – Richard Feldman](https://www.youtube.com/watch?v=QyJZzq0v7Z4)
[Intro to Python Mocks](https://www.youtube.com/watch?v=smPbDqGjFAI)
[Learn Pytest in 60 Minutes : Python Unit Testing Framework](https://www.youtube.com/watch?v=bbp_849-RZ4)

[New Features in Python 3.10  Towards Data Science ](https://towardsdatascience.com/new-features-in-python-3-10-66ac05e62fc7)
[Python Will be Dead in 2021?  by Rizky Maulana N  Towards Data Science ](https://towardsdatascience.com/python-will-be-dead-in-2021-bdbc28400996)
[LinkedIn API + Python = Programmatically Publishing  by Alessandro Berti  Towards Data Science ](https://towardsdatascience.com/linkedin-api-python-programmatically-publishing-d88a03f08ff1)
[If your Python code throws errors, check these things first  by Rhea Moutafis  Nov, 2020  Towards Data Science ](https://towardsdatascience.com/if-your-python-code-throws-errors-check-these-things-first-a93d8a9036f1)
[Mastering Anonymous Functions in Python  by Sadrach Pierre, Ph.D.  Nov, 2020  Towards Data Science ](https://towardsdatascience.com/mastering-anonymous-functions-in-python-75bcd4332dfa)
[Mastering String Methods in Python  by Julian Herrera  Nov, 2020  Towards Data Science ](https://towardsdatascience.com/mastering-string-methods-in-python-456174ede911)
[Mastering String Methods in Python  by Julian Herrera  Nov, 2020  Towards Data Science ](https://towardsdatascience.com/mastering-string-methods-in-python-456174ede911)
[Iterables and Iterators in Python  by Luay Matalka  Nov, 2020  Towards Data Science ](https://towardsdatascience.com/iterables-and-iterators-in-python-849b1556ce27)

[Mastering Anonymous Functions in Python  by Sadrach Pierre, Ph.D.  Nov, 2020  Towards Data Science ](https://towardsdatascience.com/mastering-anonymous-functions-in-python-75bcd4332dfa)

python
  feature list
    type hints
ai stuff
quincy larson freecodecamp tuts
[Python — From Intermediate to Superhero  by Negoiţă D. D. Felix  Noteworthy - The Journal Blog ](https://blog.usejournal.com/python-from-intermediate-to-superhero-1a86e518bb77)
[A Step-By-Step Guide To Building a Trading Bot In Any Programming Language  by Yakko Majuri  Aug, 2020  Medium ](https://medium.com/@yakko.majuri/a-step-by-step-guide-to-building-a-trading-bot-in-any-programming-language-d202ffe91569)

[Python, for Experienced Programmers  by Jamie Bullock  Dev Genius  Jul, 2020](https://medium.com/dev-genius/python-for-experienced-programmers-a2ee334ce62f)
[Five Python Features You (Probably) Didn’t Know  by James Briggs  Jul, 2020](https://towardsdatascience.com/five-python-features-you-probably-didnt-know-d48faa0b892e)

PyCoder's Weekly <admin@pycoders.com> - bloody amazing!

`six.text_type`
>Type for representing (Unicode) textual data. This is `unicode()` in Python 2 and `str` in Python 3.
[six](/../../pl/python/misc/six.md)


[Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk)
and the other stuff from him
[The Mental Game of Python - Raymond Hettinger](https://www.youtube.com/watch?v=UANN2Eu6ZnM)


[Python in the Movies, Reading Crazy Excel Files, Exploring Fractals, and More - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/?ui=2&view=btop&ver=1cid59g061n3t&search=inbox&th=%23thread-f%3A1681101190819999726&cvid=4)

[Pandas DataFrame (Python): 10 useful tricks - Level Up Coding ](https://levelup.gitconnected.com/pandas-dataframe-python-10-useful-tricks-b4beae91df3d)
[Asyncio — Moving towards the asynchronous future of Python ](https://medium.com/analytics-vidhya/asyncio-moving-towards-the-async-future-of-python-28d3231608)
[Understand __slots__ in Python - Towards Data Science ](https://towardsdatascience.com/understand-slots-in-python-e3081ef5196d)
[Why every Pythonista must-read “Automate the boring stuff with Python”? ](https://medium.com/swlh/why-every-pythonista-must-read-automate-the-boring-stuff-with-python-2ba31e8843df)

[Why every Pythonista must-read “Automate the boring stuff with Python”?  Vishal Sharma in The Startup - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/#inbox/FMfcgxwHNqDcprFWDzgVkLfFSLPkTSfl)
>Bible for Python Programmers!

[python/cmdline/argparse.md](file:///Users/kvogel/Projects/python/cmdline/argparse.md)
[Containerized Python Development - Part 1 - Docker Blog ](https://www.docker.com/blog/containerized-python-development-part-1/)
  try, grok

[Notifications & Updates for You: The Real Python Podcast – Episode #11: Advice on Getting Started With Testing in Python - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/#inbox/FMfcgxwHNgWwSKHKMjWSBVjLdfzCQwxL)
[Notifications & Updates – Real Python ](https://realpython.com/account/notifications/?utm_campaign=2020-05-29)
[Build Physical Projects With Python on the Raspberry Pi – Real Python ](https://realpython.com/preview/python-raspberry-pi/)
[Episode #11: Advice on Getting Started With Testing in Python – The Real Python Podcast ](https://realpython.com/podcasts/rpp/11/)

  [rais.io ](https://www.rais.io/)
  [tornado python](https://www.google.com/search?q=tornado+python)
    [Tornado Web Server — Tornado 6.0.4 documentation ](https://www.tornadoweb.org/en/stable/)
    [Push technology - Wikipedia ](https://en.wikipedia.org/wiki/Push_technology#Long_polling)
    [WebSocket - Wikipedia ](https://en.wikipedia.org/wiki/WebSocket)
    [User’s guide — Tornado 6.0.4 documentation ](https://www.tornadoweb.org/en/stable/guide.html)
    [WSGI — WSGI.org ](https://wsgi.readthedocs.io/en/latest/)
    [Tornado  Read the Docs ](https://readthedocs.org/projects/tornado/downloads/)

[Stop Using Square Bracket Notation to Get a Dictionary’s Value in Python  by Jonathan Hsu  Better Programming  Medium ](https://medium.com/better-programming/stop-using-square-bracket-notation-to-get-a-dictionarys-value-in-python-c617f6ea15a3)
```py
author = {
   "first_name": "Jonathan",
   "last_name": "Hsu",
   "username": "jhsu98"
}
print(author.get('middle_initial', None)) # None
print(author.setdefault('middle_initial',None)) # None
print(author)
"""
{
  'first_name': 'Jonathan',
  'last_name': 'Hsu',
  'username': 'jhsu98',
  'middle_initial': None
}
"""
```

### cls, staticmethod and classmethod

[cls python](https://www.google.com/search?q=cls+python)
[python - Difference between staticmethod and classmethod](https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod)


[python sentinel](https://www.google.com/search?q=python+sentinel&ie=UTF-8)
[What is the point of "sentinel object" pattern in Python](https://stackoverflow.com/questions/61105825/what-is-the-point-of-sentinel-object-pattern-in-python)
[The Sentinel Object Pattern ](https://python-patterns.guide/python/sentinel-object/)
[Model field reference  Django documentation  Django ](https://docs.djangoproject.com/en/dev/ref/models/fields/#null)
```
PS C:\Users\cbird> wsl
20/08/14 7:34:52 kvogel-elitebook:~
❯ bpython
bpython version 0.17.1 on top of Python 2.7.15rc1 /usr/bin/python
```
```py
>>> sentinel = object()
>>> sentinel
<object object at 0x7f332cade5e0>
>>> s2 = object()
>>> s2
<object object at 0x7f332cade600>
>>>
```

>I have a rule of thumb, no logic in loops, it is one method's responsibility to iterate, and an other method's to execute the logic.

[module - What does a . in an import statement in Python mean?](https://stackoverflow.com/questions/7279810/what-does-a-in-an-import-statement-in-python-mean)



a generator is a routine that can be used to control the iteration behaviour of a loop. All generators are also iterators.
A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values. However, instead of building an array containing all the values and returning them all at once, a generator yields the values one at a time, which requires less memory and allows the caller to get started processing the first few values immediately.
In short, a *generator looks like a function but behaves like an iterator*.

learn-django repo...

[New Poll: What Python IDE / Editor you used the most in 2020? ](https://www.kdnuggets.com/2020/09/poll-python-ide-editor.html)
[Automating Every Aspect of Your Python Project ](https://www.kdnuggets.com/2020/09/automating-every-aspect-python-project.html)
[Data Science Minimum: 10 Essential Skills You Need to Know to Start Doing Data Science ](https://www.kdnuggets.com/2020/10/data-science-minimum-10-essential-skills.html)

[Introduction to Time Series Analysis in Python; 10 Essential Skills You Need to Know to Start Doing Data Science - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/#inbox/FMfcgxwJZJWQrFMpdjLtrXZvBvphtzdB)
[Vladislav Zorov's answer to If Python has such poor performance (compared to Java, C++, etc.), how and why is Django so fast? ](https://www.quora.com/If-Python-has-such-poor-performance-compared-to-Java-C-etc-how-and-why-is-Django-so-fast/answer/Vladislav-Zorov)

[Pythonic code course: the list comprehension - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/#inbox/FMfcgxwJZJRplRvJNpTSLfJxJKfKHVCP)
[Pythonic code: the list comprehension · Matt Layman ](https://www.mattlayman.com/blog/2017/pythonic-code-the-list-comprehension/)

[python developer roadmap](https://www.google.com/search?q=python+developer+roadmap&ved=2ahUKEwiFkeCbkKDrAhWRh1wKHWGuDggQ1QIoAnoECAwQAw)
[A realistic roadmap to becoming a Python developer  Hacker Noon ](https://hackernoon.com/a-realistic-roadmap-to-becoming-a-python-developer-ab5872959509)
[Python Road Map — How To Become A Python Developer?  by Aayushi Johari  Edureka  Medium ](https://medium.com/edureka/how-to-become-a-python-developer-462a0093f246)
[The Ultimate Python Roadmap - 2020  Slither into Python ](https://www.slitherintopython.com/blog/posts/ultimate-python-roadmap-2020.html)
[Learn Python For Free in 2020  Slither into Python ](https://www.slitherintopython.com/)
[MatthieuDasnoy/python-developer-roadmap: A roadmap to becoming a Python developer ](https://github.com/MatthieuDasnoy/python-developer-roadmap)

[python benefits of dynamic typing](https://www.google.com/search?q=python+benefits+of+dynamic+typing&ie=UTF-8)
[What is the supposed productivity gain of dynamic typing? - Software Engineering Stack Exchange ](https://softwareengineering.stackexchange.com/questions/122205/what-is-the-supposed-productivity-gain-of-dynamic-typing)
[Why is Python a dynamic language and also a strongly typed language - Python Wiki ](https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language)

[Building a Python UI for Comparing Data  by Costas Andreou  Towards Data Science ](https://towardsdatascience.com/building-a-python-ui-for-comparing-data-13c10693d9e4)
[4 Simple Ways to Refactor Your Python Code  by Jonathan Hsu  Code 85  Medium ](https://medium.com/code-85/4-simple-ways-to-refactor-your-python-code-2f491b767381)

[PyCharm vs VSCode. Is it time to change your IDE?  by Sohaib Ahmad  Jun, 2020  Towards Data Science ](https://towardsdatascience.com/pycharm-vs-vscode-9ffbed46ac9e)

[falcon framework](https://www.google.com/search?q=falcon+framework&ie=UTF-8)
[The Falcon Web Framework — Falcon 2.0.0 documentation ](https://falcon.readthedocs.io/en/stable/)
[786 TRY IT NOW](https://www.google.com/search?q=786+TRY+IT+NOW&ie=UTF-8)
[Doug Tarr on Twitter: "HTTP 786 - Try it Now #devhumor https://t.co/U8dyaHIS6n" / Twitter ](https://twitter.com/doug_tarr/status/444582252391825408)
[joho/7XX-rfc: An RFC for a new series of HTTP status codes covering developer fouls. ](https://github.com/joho/7XX-rfc)
[Http status codes explained - ict.ken.be ](https://ict.ken.be/http-status-codes-explained)
[The Falcon Web Framework — Falcon 0.2.0rc1 documentation ](https://falcon.readthedocs.io/en/0.2.0/)
[Falcon  The minimal, fast, and secure web framework for Python ](https://falconframework.org/)
[falconry/falcon: The no-nonsense, minimalist web services and app backend framework for Python developers with a focus on reliability, correctness and performance at scale. ](https://github.com/falconry/falcon)
[falcon vs flask](https://www.google.com/search?q=falcon+vs+flask&ved=2ahUKEwiGv9Sk8cXqAhWpSRUIHeEWA_QQ1QIoAHoECA0QAQ)
[Falcon vs. Flask — Which one to pick to create a scalable deep learning REST API  by Dat Tran  idealo Tech Blog  Medium ](https://medium.com/idealo-tech-blog/falcon-vs-flask-which-one-to-pick-to-create-a-scalable-deep-learning-rest-api-adef647ebdec#:~:text=Falcon%20is%20like%20Flask%2C%20a,and%20the%20REST%20architectural%20style.)
[Building a simple Keras + deep learning REST API ](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)
[Building Very Fast App Backends with Falcon Web Framework on PyPy - Alibaba Cloud Community ](https://www.alibabacloud.com/blog/building-very-fast-app-backends-with-falcon-web-framework-on-pypy_594282)
[Falcon  The minimal, fast, and secure web framework for Python ](https://falconframework.org/?spm=a2c65.11461447.0.0.41b076d9gHh2OB#sectionBenchmarks)
[Cythonized](https://www.google.com/search?q=Cythonized&ie=UTF-8)
[Home · falconry/falcon Wiki · GitHub ](https://github.com/falconry/falcon/wiki)

[Compatible with PyPy](https://www.google.com/search?q=Compatible+with+PyPy&ie=UTF-8)
[PyPy ](https://www.pypy.org/#:~:text=Compatibility%3A%20PyPy%20is%20highly%20compatible,micro%2Dthreads%20for%20massive%20concurrency.)

[The Simplest Way to Create Visualizations in Python Isn’t With matplotlib.  by Andre Ye  Jul, 2020  Towards Data Science ](https://towardsdatascience.com/the-simplest-way-to-create-complex-visualizations-in-python-isnt-with-matplotlib-a5802f2dba92)

[30 Magical Python Tricks to Write Better Code](https://towardsdatascience.com/30-magical-python-tricks-to-write-better-code-e54d1642c255)
[How to Define Custom Exception Classes in Python - Towards Data Science ](https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca)
[10 Tools I Use to Craft Better Python Code - Level Up Coding ](https://levelup.gitconnected.com/10-tools-i-use-to-craft-better-python-code-b9a9776a7871)

[Step-up Your RegEx Game in Python  James Briggs in Towards Data Science - chrisjbird@gmail.com - Gmail ](https://mail.google.com/mail/u/0/#inbox/FMfcgxwJWXXVmCvbpkMrcXztKPRQnjfm)
[Level Up For-Loops in Python With 4 Simple Functions ](https://medium.com/swlh/level-up-for-loops-in-python-with-4-simple-functions-da01173a834c)

[Python Job Board – Python Jobs HQ ](https://www.pythonjobshq.com/?__s=5r8stehqp1fcvezhd5ng)
[Managing Python Dependencies – Real Python ](https://realpython.com/products/managing-python-dependencies/?utm_content=mpd&__s=5r8stehqp1fcvezhd5ng)
[Python Tricks: The Book – Real Python ](https://realpython.com/products/python-tricks-book/?utm_content=pytricksbook&__s=5r8stehqp1fcvezhd5ng)
[Python Basics Book – Real Python ](https://realpython.com/products/python-basics-book/?utm_content=pybasicsbook&__s=5r8stehqp1fcvezhd5ng)
[Office Hours – Real Python ](https://realpython.com/office-hours/?__s=5r8stehqp1fcvezhd5ng)
[Episode #18: Ten Years of Flask: Conversation With Creator Armin Ronacher – The Real Python Podcast ](https://realpython.com/podcasts/rpp/18/)
[Pandas Project: Make a Gradebook With Python & Pandas – Real Python ](https://realpython.com/pandas-project-gradebook/?__s=5r8stehqp1fcvezhd5ng)
[Learn IP Address Concepts With Python's ipaddress Module – Real Python ](https://realpython.com/python-ipaddress-module/?__s=5r8stehqp1fcvezhd5ng)
[Grow Your Python Portfolio With 13 Intermediate Project Ideas – Real Python ](https://realpython.com/courses/intermediate-project-ideas/)

[how can I find out which python virtual environment I am using?](https://stackoverflow.com/questions/53952214/how-can-i-find-out-which-python-virtual-environment-i-am-using)

`bpython` uses anaconda! why??
```
(venv) 20/07/15 21:37:40 kvogel-macbook-2018:~/Projects-work/skoot/api/microservices ±(master) ✗ 
❯ bpython
bpython version 0.18 on top of Python 3.7.3 /usr/local/anaconda3/bin/python
```
```py
>>> import sys
>>> sys.prefix
'/usr/local/anaconda3'
```

```
(venv) 20/07/15 21:50:50 kvogel-macbook-2018:~/Projects-work/skoot/api/microservices ±(master) ✗ 
❯ python
Python 3.7.3 | packaged by conda-forge | (default, Jul  1 2019, 14:38:56) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
```
```py
>>> import sys
>>> sys.prefix
'/Users/kvogel/Projects-work/skoot/api/microservices/talon_one/coupons/venv'
```

```py
    Groupable = collections.namedtuple('Groupable', ('rdr_entry', 'closer',
                                                     'sender', 'row'))
```
?

[python __all__](https://www.google.com/search?q=python+__all__&ie=UTF-8)
[syntax - Can someone explain __all__ in Python?](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)
[Why should I use __all__ in __init__ of python package?](https://stackoverflow.com/questions/30888683/why-should-i-use-all-in-init-of-python-package)

[python from dot import](https://www.google.com/search?q=python+from+dot+import)
[python - `from ... import` vs `import .`](https://stackoverflow.com/questions/9439480/from-import-vs-import)
[Absolute vs Relative Imports in Python – Real Python ](https://realpython.com/absolute-vs-relative-python-imports/)
[Python "from dotpackage import ..." syntax](https://stackoverflow.com/questions/22511792/python-from-dotpackage-import-syntax)
[module - What does a . in an import statement in Python mean?](https://stackoverflow.com/questions/7279810/what-does-a-in-an-import-statement-in-python-mean)
[6. Modules — Python 3.8.4 documentation ](https://docs.python.org/3/tutorial/modules.html)
[PEP 328 -- Imports: Multi-Line and Absolute/Relative  Python.org ](https://www.python.org/dev/peps/pep-0328/)
[Python-Dev PEP 328 -- relative and multi-line import ](https://mail.python.org/pipermail/python-dev/2004-March/043739.html)
[python - Importing with dot notation](https://stackoverflow.com/questions/45593981/importing-with-dot-notation)


[vscode python venv](https://www.google.com/search?q=vscode+python+venv&ie=UTF-8)
[VS Code Doesn't Recognize Python Virtual Environment](https://stackoverflow.com/questions/56652968/vs-code-doesnt-recognize-python-virtual-environment)
[python - Auto activate virtual environment in Visual Studio Code](https://stackoverflow.com/questions/58433333/auto-activate-virtual-environment-in-visual-studio-code)

[How to setup virtual environment for Python in VS Code?](https://stackoverflow.com/questions/54106071/how-to-setup-virtual-environment-for-python-in-vs-code)
>-I have been using vs code for a while now and found an another way to show virtual environments in vs code.
>Go to the parent folder in which venv is there through command prompt.
>Type `code .` and Enter. [Working on both windows and linux for me.]
>That should also show the virtual environments present in that folder.

So what can super() do for you in single inheritance?

Like in other object-oriented languages, it allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.

[python super](https://www.google.com/search?q=python+super&ie=UTF-8)
[Supercharge Your Classes With Python super() – Real Python ](https://realpython.com/python-super/)
[class - Understanding Python super() with __init__() methods](https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods)
[oop - What does 'super' do in Python?](https://stackoverflow.com/questions/222877/what-does-super-do-in-python)
>The benefits of super() in single-inheritance are minimal -- mostly, you don't have to hard-code the name of the base class into every method that uses its parent methods.
>However, it's almost impossible to use multiple-inheritance without super(). This includes common idioms like mixins, interfaces, abstract classes, etc. This extends to code that later extends yours. If somebody later wanted to write a class that extended Child and a mixin, their code would not work properly.

[MRO (Method Resolution Order)](https://www.google.com/search?q=MRO+(Method+Resolution+Order)&ie=UTF-8)
[Method Resolution Order (MRO) in Python ](http://www.srikanthtechnologies.com/blog/python/mro.aspx)
[python - Method Resolution Order (MRO) in new-style classes?](https://stackoverflow.com/questions/1848474/method-resolution-order-mro-in-new-style-classes)

[Python Objects and Classes: The Most Important Python Concepts That You Need to Understand  Towards Data Science ](https://towardsdatascience.com/the-most-important-python-concept-that-you-need-to-understand-985b98bbb84)
[Features You Likely Don’t Use in Python 3 — But You Should  by Amritansh Sagar  Jul, 2020  Towards Data Science ](https://towardsdatascience.com/features-you-likely-dont-use-in-python-3-but-you-should-2d79dba4cfb3)

[Learning Python 10 minutes a day #13  by Dennis Bakhuis  Jul, 2020  Towards Data Science ](https://towardsdatascience.com/learning-python-10-minutes-a-day-13-4d8172df24b2)
[The Most Elegant Python Object-Oriented Programming  by Christopher Tao  Jul, 2020  Towards Data Science ](https://towardsdatascience.com/the-most-elegant-python-object-oriented-programming-b38d75f4ae7b)
[How to integrate Excel with Python  Towards Data Science ](https://towardsdatascience.com/invigorate-excel-with-python-58c9c3208093)

[Learning Python 10 minutes a day #14  by Dennis Bakhuis  Jul, 2020  Towards Data Science ](https://towardsdatascience.com/learning-python-10-minutes-a-day-14-da2cc6a05c59)
[Python Fundamentals To Become a True Programmer, Part 1  by Dorel Masasa  Jul, 2020  Towards Data Science ](https://towardsdatascience.com/python-fundemtales-to-become-a-true-programmer-part-1-d9962f7eca6d)
python import dot notation

[avoid if else](https://www.google.com/search?q=avoid+if+else&ie=UTF-8)
[coding style - Clarification of "avoid if-else" advice - Software Engineering Stack Exchange ](https://softwareengineering.stackexchange.com/questions/206816/clarification-of-avoid-if-else-advice)
[Why you should avoid conditional statements ](http://www.thedevpiece.com/why-you-should-avoid-if-else-statements/)

### [caching in django](https://www.google.com/search?q=caching+in+django&ie=UTF-8)

[Caching in Django  TestDriven.io ](https://testdriven.io/blog/django-caching/)
[Django Caching - It's Easy if you do it in the Smart Way! - DataFlair ](https://data-flair.training/blogs/django-caching/)

[Caching in Django With Redis – Real Python ](https://realpython.com/caching-in-django-with-redis/)
>Redis is an in-memory data structure store that can be used as a caching engine. Since it keeps data in RAM, Redis can deliver it very quickly. 
>Memcached is another popular in-memory caching system, but many people agree that Redis is superior to Memcached in most circumstances. Personally, we like how easy it is to set up and use Redis for other purposes such as Redis Queue.

redis grok...
django caching grok...
tdd, etc grok...


>Python is popular in fintech startups; higher up it's C#, Java, Golang - [Jack Barry - Fintech Specialist](https://mail.google.com/mail/u/0/#inbox/FMfcgxwLsJvLCLKzzGMzwCfCbWSQGcxC)

blog/210202-pycharm-wsl.md

[pdoc 📚 ](https://pdoc.dev/)
>pdoc auto-generates API documentation that follows your project's Python module hierarchy.

notes/wsgi.md

blog/210202-os.md

environment/pipenv.md

[Distributing python packages protected with Cython  by Artem Vasilyev  The Startup  Medium ](https://medium.com/swlh/distributing-python-packages-protected-with-cython-40fc29d84caf)

