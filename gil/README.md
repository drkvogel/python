


[python gil](https://www.google.co.uk/search?q=python+gil&ie=UTF-8)
[Global interpreter lock - Wikipedia ](https://en.wikipedia.org/wiki/Global_interpreter_lock)
[Explain python global interpreter lock (GIL) Like I'm Five - DEV Community 👩‍💻👨‍💻 ](https://dev.to/docoprusta/explain-python-global-interpreter-lock-gil-like-im-five-25k8)
[pypy gil](https://www.google.co.uk/search?q=pypy+gil)
[Frequently Asked Questions — PyPy documentation ](http://doc.pypy.org/en/latest/faq.html)
[PyPy Status Blog: Let's remove the Global Interpreter Lock ](https://morepypy.blogspot.com/2017/08/lets-remove-global-interpreter-lock.html)
[Parallelism is very bad on CPython and PyPy; GIL was added because the early p...  Hacker News ](https://news.ycombinator.com/item?id=13485438)

>The GIL prevents any two threads from simultaneously executing python
bytecode instructions. However, when there is IO to be performed, represented
by going to the post office, a thread will release the GIL so that other
threads can execute python bytecode instructions.

>The GIL doesn't prevent computation in general, just the interpretation of
python bytecode. High-performance numerical packages like Numpy perform
operations on large arrays of data using machine instructions, and are
generally written in C or another compiled language. While these large
computations are being performed, the thread can release the GIL since
it isn't manipulating python objects outside its array of numerical data.

[Python language has its own reasons to use GIL](https://www.google.com/search?q=Python+language+has+its+own+reasons+to+use+GIL&ie=UTF-8)
[multithreading - Why Was Python Written with the GIL? - Software Engineering Stack Exchange ](https://softwareengineering.stackexchange.com/questions/186889/why-was-python-written-with-the-gil)
[python - Why the Global Interpreter Lock?](https://stackoverflow.com/questions/265687/why-the-global-interpreter-lock)
[What is the Python Global Interpreter Lock (GIL)? – Real Python ](https://realpython.com/python-gil/)
[Global interpreter lock - Wikipedia ](https://en.wikipedia.org/wiki/Global_interpreter_lock)
[Security with Go: Explore the power of Golang to secure host, web, and cloud ... - John Daniel Leon - Google Books ](https://books.google.co.th/books?id=pSZKDwAAQBAJ&pg=PA16&lpg=PA16&dq=Python+language+has+its+own+reasons+to+use+GIL&source=bl&ots=AYt1hQjJ1i&sig=ACfU3U2m2QPmx5DM3P7VGmEwYZPBBb7lDQ&hl=en&q=Python%20language%20has%20its%20own%20reasons%20to%20use%20GIL&f=false)
[Pragmatic Python GIL in 3 Minutes - Sriram Sundarraj’s blog ](https://blog.ssundarraj.me/the-python-gil-in-2-minutes-80d74d56a1a0)
[Understanding the Python GIL](https://www.youtube.com/watch?v=Obt-vMVdM8s)
[Everything I know about Global Interpreter Lockers(GIL) ](https://medium.com/@geisonfgfg/everything-i-know-about-global-interpreter-lockers-gil-880e1f4c45e0)
