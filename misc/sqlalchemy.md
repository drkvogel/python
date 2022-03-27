

[Library - SQLAlchemy ](https://www.sqlalchemy.org/library.html#architecture)

SQLAlchemy levels:
(Raw? ->) Core -> Expression Language -> ORM?
Raw -> Core (1.x style and 2.0 style, using Expression Language) -> ORM?

>If you want to view your data in a more *schema-centric view (as used in SQL)*, use Core. If you have *data for which business objects are not needed*, use Core. If you view your data as business objects, use ORM.

>As of SQLAlchemy 1.4, there are two distinct styles of Core use known as 1.x style and 2.0 style, the latter of which makes some adjustments mostly in the area of how transactions are controlled as well as narrows down the patterns for how SQL statement constructs are executed.

### Raw SQL in SQLAlchemy

[How to execute raw SQL queries in SQLAlchemy in Python ](https://www.adamsmith.haus/python/answers/how-to-execute-raw-sql-queries-in-sqlalchemy-in-python)
>Use `sqlalchemy.sql.expression.text()` to execute raw sql queries in sqlalchemy
>Call `sqlalchemy.sql.expression.text(string)` with a SQL query string to create a new SQLAlchemy `TextClause` object directly representing the given textual SQL query.
>Call `connectable.execute(TextClause)` to execute the previous result `TextClause` with connectable as either an SQLAlchemy Connection, Session or Engine, returning an SQLAlchemy `ResultProxy`.
>Use `Session` if you are using the ORM functionality. Use `Connection` *if you are doing SQL queries not bound to objects*, or need more granular control over the database connection (like for transactions).
>Call `ResultProxy.fetchall()` with the previous result `ResultProxy` to get the results of the executed query as a list of tuples.


### SQLAlchemy Expression Language

SQLAlchemy Core uses SQLAlchemy Expression Language?

[SQLAlchemy Core — SQLAlchemy 1.4 Documentation ](https://docs.sqlalchemy.org/en/14/core/)
[SQL Expression Language Tutorial (1.x API) — SQLAlchemy 1.4 Documentation ](https://docs.sqlalchemy.org/en/14/core/tutorial.html)
  notice Expression Language is under core...

>The SQLAlchemy Expression Language presents a system of representing relational database structures and expressions using Python constructs.

[Introduction to SQLAlchemy Expression Language | by Ng Wai Foong | Level Up Coding ](https://levelup.gitconnected.com/introduction-to-sqlalchemy-expression-language-6943894bbf7)

>SQLAlchemy Expression Language: “… presents a system of representing relational database structures and expressions using Python constructs. These constructs are modeled to resemble those of the underlying database as closely as possible, while providing a modicum of abstraction of the various implementation differences between database backends. While the constructs attempt to represent equivalent concepts between backends with consistent structures, they do not conceal useful concepts that are unique to particular subsets of backends. The Expression Language therefore presents a method of writing backend-neutral SQL expressions, but does not attempt to enforce that expressions are backend-neutral.”
>SQLAlchemy is famous for its Object-Relational Mapper, which is a *distinct API that builds on top of the Expression Language*.

[sqlalchemy Tutorial => Hello, World! (SQLAlchemy Core) ](https://riptutorial.com/sqlalchemy/example/14691/hello--world---sqlalchemy-core-)


[How to Execute Raw SQL in SQLAlchemy | Tutorial by Chartio ](https://chartio.com/resources/tutorials/how-to-execute-raw-sql-in-sqlalchemy/)
[python - How to execute raw SQL in Flask-SQLAlchemy app](https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app)
[python - executing a raw sql query from sqlalchemy on postgresql](https://stackoverflow.com/questions/49565415/executing-a-raw-sql-query-from-sqlalchemy-on-postgresql)


[SQLAlchemy](https://en.wikipedia.org/wiki/SQLAlchemy)
>SQLAlchemy's philosophy is that relational databases behave less like object collections as the scale gets larger and performance starts being a concern, while object collections behave less like tables and rows as more abstraction is designed into them. For this reason it has adopted the *data mapper pattern* (similar to Hibernate for Java) *rather than the active record pattern* used by a number of other object-relational mappers.[6] However, optional plugins allow users to develop using declarative syntax.

[Active record pattern](https://en.wikipedia.org/wiki/Active_record_pattern)
>the active record pattern is considered an architectural pattern by some people and as an anti-pattern by some others recently
>A database table or view is wrapped into a class. Thus, an object instance is tied to a single row in the table. After creation of an object, a new row is added to the table upon save. Any object loaded gets its information from the database. When an object is updated, the corresponding row in the table is also updated. The wrapper class implements accessor methods or properties for each column in the table or view.
```js
part = new Part()
part.name = "Sample part"
part.price = 123.45
part.save()
```
[Data mapper pattern](https://en.wikipedia.org/wiki/Data_mapper_pattern)
> The interface of an object conforming to this pattern would include functions such as Create, Read, Update, and Delete, that operate on objects that represent domain entity types in a data store.
>Python SQLAlchemy library
>A Data Mapper is a Data Access Layer that performs bidirectional transfer of data between a persistent data store (often a relational database) and an in-memory data representation (the domain layer). The goal of the pattern is to keep the in-memory representation and the persistent data store independent of each other and the data mapper itself. This is useful when one needs to model and enforce strict business processes on the data in the domain layer that do not map neatly to the persistent data store.[2] The layer is composed of one or more mappers (or Data Access Objects), performing the data transfer. Mapper implementations vary in scope. Generic mappers will handle many different domain entity types, dedicated mappers will handle one or a few.
