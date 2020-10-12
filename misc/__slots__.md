
[__slots__](https://www.google.com/search?q=__slots__&ie=UTF-8)
[python - Usage of __slots__?](https://stackoverflow.com/questions/472000/usage-of-slots)


[10. __slots__ Magic — Python Tips 0.1 documentation ](https://book.pythontips.com/en/latest/__slots__magic.html)
>10. __slots__ Magic
>In Python every class can have instance attributes. By default Python uses a dict to store an object’s instance attributes. This is really helpful as it allows setting arbitrary new attributes at runtime.
>However, for small classes with known attributes it might be a bottleneck. The dict wastes a lot of RAM. Python can’t just allocate a static amount of memory at object creation to store all the attributes. Therefore it sucks a lot of RAM if you create a lot of objects (I am talking in thousands and millions). Still there is a way to circumvent this issue. It involves the usage of `__slots__` to tell Python not to use a dict, and only allocate space for a fixed set of attributes.

>you might want to give PyPy a try. It does all of these optimizations by default.


[A quick dive into Python’s “__slots__”  by Stephen Jayakar  Noteworthy - The Journal Blog ](https://blog.usejournal.com/a-quick-dive-into-pythons-slots-72cdc2d334e)
