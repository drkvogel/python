
[Marshalling (computer science)](https://en.wikipedia.org/wiki/Marshalling_(computer_science))
>Marshalling (or serialization) is the operation when we take an arbitrary data structure and convert it into a string in a way that we can convert the string back to the same data structure.
>Marshalling can be used to save data persistent between execution of the same script, to transfer data between processes, or even between machines. In some cases it can be used to communicate between two processes written in different programming languages.
>The marshal module provides such features but it is not recommended as it was built for internal object serialization for python.
>The pickle module was designed for this task. The json module can be used too.

[marshal_with](https://www.google.com/search?qie=UTF-8)
[Response marshalling — Flask-RESTPlus 0.13.0 documentation ](https://flask-restplus.readthedocs.io/en/stable/marshalling.html)
[Marshal_with flask-RESTX](https://www.google.com/search?qsadpr=1.41)
[Response marshalling — Flask-RESTX 0.5.2.dev documentation ](https://flask-restx.readthedocs.io/en/latest/marshalling.html)
[How do I marshal a list of objects? · Issue #300 · flask-restful/flask-restful ](https://github.com/flask-restful/flask-restful/issues/300)
[Python Flask_restplus flash_restx dynamic marshalling response](https://stackoverflow.com/questions/63849014/python-flask-restplus-flash-restx-dynamic-marshalling-response)
[Dynamically marshalling output in Flask Restplus | blog.fossasia.org ](https://blog.fossasia.org/dynamically-marshaling-output-in-flask-restplus/)
[Access required ](https://uhsnhs.sharepoint.com/sites/ChilworthProject/_layouts/15/AccessDenied.aspx?Sourcecorrelation=e7001fa0-609e-3000-9f5e-4d963e314b95)
[python what is marshalling](https://www.google.com/search?qie=UTF-8)
[Marshalling / Serialization ](https://code-maven.com/slides/python/marshalling#:~:texttext=The%20marshal%20module%20provides%20such,internal%20object%20serialization%20for%20python.)
[marshal — Internal Python object serialization — Python 3.10.2 documentation ](https://docs.python.org/3/library/marshal.html)
>`marshal` — Internal Python object serialization
>This module contains functions that can *read and write Python values in a binary format*. The format is *specific to Python*, but independent of machine architecture issues (e.g., you can write a Python value to a file on a PC, transport the file to a Sun, and read it back there). Details of the format are undocumented on purpose; it may change between Python versions (although it rarely does). 1

>This is *not a general “persistence” module*. For general persistence and transfer of Python objects through *RPC* calls, see the modules `pickle` and `shelve`. The marshal module exists mainly to support reading and writing the “pseudo-compiled” code for Python modules of `.pyc` files. Therefore, the Python maintainers reserve the right to modify the marshal format in backward incompatible ways should the need arise. If you’re serializing and de-serializing Python objects, use the `pickle` module instead – the performance is comparable, version independence is guaranteed, and `pickle` supports a substantially wider range of objects than `marshal`.

