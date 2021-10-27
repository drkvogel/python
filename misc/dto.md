
[DTO named tuple](https://www.google.com/search?q=DTO+named+tuple&ie=UTF-8)

[DTOs in Python : Python ](https://www.reddit.com/r/Python/comments/ecw5gq/dtos_in_python/)
>objects that are used to pass data between functions and are not entities or basic types
>three typed options: `NamedTuple`, `dataclass` and `TypedDict`

>pydantic !!!! https://pydantic-docs.helpmanual.io/


[Records, Structs, and Data Transfer Objects in Python – dbader.org ](https://dbader.org/blog/records-structs-and-data-transfer-objects-in-python)
>Which type should I use for data objects in Python? As you’ve seen there’s quite a number of different options to implement records or data objects in Python. Generally your decision will depend on your use case:

>* You only have a few (2-3) fields: Using a plain *tuple* object may be okay because the field order is easy to remember or field names are superfluous. For example, think of an `(x, y, z)` point in 3D space.
>* You need immutable fields: In this case plain tuples, `collections.namedtuple`, `typing.NamedTuple` would all make good options for implementing this type of data object.
>* You need to lock down field names to avoid typos: `collections.namedtuple` and `typing.NamedTuple` are your friends.
>* You want to keep things simple: A plain *dictionary* object might be a good choice due to the convenient syntax that closely resembles JSON.
>* You need full control over your data structure: It’s time to write a custom *class* with `@property` setters and getters.
>* You need to add behavior (methods) to the object: You should write a custom *class*. Either from scratch or by extending `collections.namedtuple` or `typing.NamedTuple`.
>* You need to pack data tightly to *serialize* it to disk or send it over the network: Time to bust out `struct.Struct`, this is a great use case for it.

>If you’re looking for a safe default choice, my general recommendation for implementing a plain record, struct, or data object in Python would be to:

>use `collections.namedtuple` in *Python 2.x*; and
>its younger sibling `typing.NamedTuple` in *Python 3*.

[stribny/python-data-structures: Python data structures ](https://github.com/stribny/python-data-structures)
[Home - attrs 20.3.0 documentation ](https://www.attrs.org/en/stable/)

[Messenger/Data Transfer Object — Python 3 Patterns, Recipes and Idioms](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Messenger.html)

[Python: Data Transfer Object](https://stackoverflow.com/questions/10920508/python-data-transfer-object)
[The Beauty of DTOs - Articles - Nico is awesome. ](https://nico.is/blog/the-beauty-of-dtos/)

[What is a Data Transfer Object (DTO)?](https://stackoverflow.com/questions/1051182/what-is-a-data-transfer-object-dto)
>A Data Transfer Object is an object that is used to encapsulate data, and send it from one subsystem of an application to another.
>DTOs are most commonly used by the Services layer in an N-Tier application to transfer data between itself and the UI layer. The main benefit here is that it reduces the amount of data that needs to be sent across the wire in distributed applications.

[P of EAA: Data Transfer Object ](https://martinfowler.com/eaaCatalog/dataTransferObject.html)
[LocalDTO ](https://martinfowler.com/bliki/LocalDTO.html)

History (chrome://history/?q=snippets)
[12 Python Snippets That Will Boost Your Productivity  by Lucas Soares  Apr, 2021  Python in Plain English ](https://python.plainenglish.io/python-snippets-7e8dcbeae26e)
[22 Python Code Snippets for Everyday Problems  by Abhay Parashar  Apr, 2021  Level Up Coding ](https://levelup.gitconnected.com/22-python-code-snippets-for-everyday-problems-4c6a216c33ae)
[10 Python Tips and “Tricks” You Have to Know  Better Programming ](https://betterprogramming.pub/10-useful-python-snippets-to-code-like-a-pro-e3d9a34e6145)
[model view controller - What is a Data Transfer Object (DTO)?](https://stackoverflow.com/questions/1051182/what-is-a-data-transfer-object-dto#:~:text=A%20Data%20Transfer%20Object%20is,itself%20and%20the%20UI%20layer.)
[P of EAA: Data Transfer Object ](https://martinfowler.com/eaaCatalog/dataTransferObject.html)
[P of EAA ](https://martinfowler.com/books/eaa.html)
Patterns of Enterprise Application Architecture
[DuplexBook ](https://martinfowler.com/bliki/DuplexBook.html)
[LocalDTO ](https://martinfowler.com/bliki/LocalDTO.html)

[Data transfer object Spatie](https://www.google.com/search?q=Data+transfer+object+Spatie&biw=1280&bih=616)
[Transforming DTOs  typescript-transformer  Spatie ](https://spatie.be/docs/typescript-transformer/v1/dtos/transforming-dtos)

[Data Transfer Objects in Python](https://www.google.com/search?q=Data+Transfer+Objects+in+Python&ie=UTF-8)
[Data Transfer Object](https://www.google.com/search?q=Data+Transfer+Object)

[Websites & webapplications in Laravel  Spatie ](https://spatie.be/)

[Articles I write ](https://romanisthere.github.io/posts/)
