
local FastAPI docs: [FastAPI](file:///home/kvogel/projects/fastapi/docs/en/site/index.html)

fastapi [demo](file:///home/kvogel/projects/general/dev/learn/python/frameworks/fastapi/demo/run)

FastAPI
>FastAPI is a modern, high-performance, *batteries-included* Python web framework that's perfect for building RESTful APIs. It can handle both synchronous and asynchronous requests and has built-in support for data validation, JSON serialization, authentication and authorization, and OpenAPI (version 3.0.2 as of writing) documentation.
>Heavily inspired by Flask, it has a lightweight microframework feel with support for Flask-like route decorators.
>It takes advantage of Python type hints for parameter declaration which enables data validation (via Pydantic) and OpenAPI/Swagger documentation.
>Built on top of Starlette, it supports the development of asynchronous APIs.
>It's fast. Since async is much more efficient than the traditional synchronous threading model, it can compete with Node and Go with regards to performance.


[Advanced User Guide - Intro - FastAPI ](https://fastapi.tiangolo.com/advanced/)

[Path Parameters and Numeric Validations - FastAPI ](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/)
[JSON Compatible Encoder - FastAPI ](https://fastapi.tiangolo.com/tutorial/encoder/)
[Body - Updates - FastAPI ](https://fastapi.tiangolo.com/tutorial/body-updates/)
[Dependencies - First Steps - FastAPI ](https://fastapi.tiangolo.com/tutorial/dependencies/)
[Middleware - FastAPI ](https://fastapi.tiangolo.com/tutorial/middleware/)
[CORS (Cross-Origin Resource Sharing) - FastAPI ](https://fastapi.tiangolo.com/tutorial/cors/)
[SQL (Relational) Databases - FastAPI ](https://fastapi.tiangolo.com/tutorial/sql-databases/)
[SQL (Relational) Databases with Peewee - FastAPI ](https://fastapi.tiangolo.com/advanced/sql-databases-peewee/)
[History, Design and Future - FastAPI ](https://fastapi.tiangolo.com/history-design-future/)
[Alternatives, Inspiration and Comparisons - FastAPI ](https://fastapi.tiangolo.com/alternatives/)
[Help FastAPI - Get Help - FastAPI ](https://fastapi.tiangolo.com/help-fastapi/)


frameworks/fastapi/starlette.md
  inc Server Push

[Path Parameters and Numeric Validations - FastAPI ](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/)
[JSON Compatible Encoder - FastAPI ](https://fastapi.tiangolo.com/tutorial/encoder/)
[Body - Updates - FastAPI ](https://fastapi.tiangolo.com/tutorial/body-updates/)

[Dependencies - First Steps - FastAPI ](https://fastapi.tiangolo.com/tutorial/dependencies/)

[Middleware - FastAPI ](https://fastapi.tiangolo.com/tutorial/middleware/)
[CORS (Cross-Origin Resource Sharing) - FastAPI ](https://fastapi.tiangolo.com/tutorial/cors/)

[APIRouter](file:///home/kvogel/projects/general/dev/learn/python/frameworks/fastapi/apirouter.md)
[Bigger Applications - Multiple Files - FastAPI ](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
[Advanced User Guide - Intro - FastAPI ](https://fastapi.tiangolo.com/advanced/)


[History, Design and Future - FastAPI ](https://fastapi.tiangolo.com/history-design-future/)
[Alternatives, Inspiration and Comparisons - FastAPI ](https://fastapi.tiangolo.com/alternatives/)

[Help FastAPI - Get Help - FastAPI ](https://fastapi.tiangolo.com/help-fastapi/)

[fastapi config](https://www.google.com/search?qie=UTF-8)
[Settings and Environment Variables - FastAPI ](https://fastapi.tiangolo.com/advanced/settings/)
[Settings management - pydantic ](https://pydantic-docs.helpmanual.io/usage/settings/)

frameworks/fastapi/fastapi-db.md

frameworks/fastapi/fastapi-performance.md

[How to Test an API with Pytest and Requests | by Travis Luong | Medium ](https://medium.com/@travisluong/how-to-test-an-api-with-pytest-and-requests-2bd52e45106d)
[Creating Effective REST APIs with FastAPI | by Ashutosh Tripathi | Medium ](https://phonx38.medium.com/creating-effective-rest-apis-with-fastapi-c85b942ec312)
[FastAPI : Testing a Database. FastAPI : Testing a Database | by Jb Rocher | Medium ](https://medium.com/@jeanb.rocher/setting-up-the-project-f24ccbec5f9f)
[Complex Request Validation in FastAPI with Pydantic.️ | by Santosh Gokul | Medium ](https://nsantoshgokul.medium.com/complex-request-validation-in-fastapi-with-pydantic-%EF%B8%8F-ef2fd297dda2)
[Dockerize your API’s: FastAPI — Part1 | by Gagandeep prasad | Towards Dev ](https://towardsdev.com/dockerize-your-apis-fastapi-part1-f44302652af9)

### uhs notes

[FastAPI ](https://fastapi.tiangolo.com/)


[The Ultimate Face-off: Flask vs. FastAPI » Developer Content from Vonage ♥ ](https://learn.vonage.com/blog/2021/08/10/the-ultimate-face-off-flask-vs-fastapi/)

[Why FastAPI?. FastAPI is a rather minimalistic… | by Ajesh Martin | featurepreneur | Medium ](https://medium.com/featurepreneur/why-fastapi-69fb172756b7)

OpenAPI/SwaggerUI, ReDoc included
types with Pydantic
validation for JSON objects (dict), JSON array (list), String (str) with min and max lengths, Numbers (int, float) with min and max values, URL, Email, UUID, and many more…
The library provides support for the followings: HTTP Basic, OAuth2 (JWT tokens), API keys in headers, query params, or cookies.

>much faster than flask because it’s built over ASGI (Asynchronous Server Gateway Interface) instead of WSGI (Web Server Gateway Interface) s the flask is built on.
>Asynchronous by nature - FastAPI supports asynchronous endpoints by default, which can simplify and make your code more efficient.

>Speed of development: In FastAPI you have *autocompletion and type hints* in your favorite IDE or code editor. That’s because the framework was built around the idea of easing the developers workload. You don’t have to install aditional plugins like Flask-Marshmallow, for validation, serialization in FastAPI. That functionality comes out of the box. In Flask, you need a plugin called Flask-Marshmallow or Flask-whatever. For instance, you need Flask-SqlAlchemy, insted of use sqlalchemy directly. In FastAPI, you can use sqlalchemy or other python libraries directly pretty easy , often with a single line of code by applying *Dependency Injection* .

Async
[Uvicorn ](https://www.uvicorn.org/) - ASGI web server
>uvloop is a fast, drop-in replacement of the built-in asyncio event loop. It is implemented in Cython
websockets
>`python-dotenv` will be installed should you want to use the `--env-file` option.
>`PyYAML` will be installed to allow you to provide a `.yaml` file to `--log-config`, if desired.
typing with Pydantic
Nice docs via ReDoc
(jwt, oauth) auth built in
>Netflix, Uber, Microsoft amongst many other corporations are using the FastAPI library


`python-dotenv`

[Understanding Flask vs FastAPI Web Framework | by Sue Lynn | Towards Data Science ](https://towardsdatascience.com/understanding-flask-vs-fastapi-web-framework-fe12bb58ee75)

[FastAPI vs Flask: Comparison Guide for Data Science Enthusiasts - ](https://analyticsindiamag.com/fastapi-vs-flask-comparison-guide-for-data-science-enthusiasts/)

[FastAPI vs Flask | Is FastAPI Right Replacement for Flask? ](https://www.analyticsvidhya.com/blog/2020/11/fastapi-the-right-replacement-for-flask/)
[REST API IN PYTHON | Flask vs. FastAPI vs. Django](https://www.youtube.com/watch?v=0juyVjBN8HQ)

[Moving from Flask to FastAPI | TestDriven.io ](https://testdriven.io/blog/moving-from-flask-to-fastapi/)

[FastAPI vs Flask - The Complete Guide ](https://christophergs.com/python/2021/06/16/python-flask-fastapi/)
[Alternatives, Inspiration and Comparisons - FastAPI ](https://fastapi.tiangolo.com/alternatives/)

[Starlette ](https://www.starlette.io/)
>Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services. It is production-ready, and gives you the following:
>* Seriously impressive performance.
>* WebSocket support.
>* In-process background tasks.
>* Startup and shutdown events.
>* Test client built on requests.
>* CORS, GZip, Static Files, Streaming responses.
>* Session and Cookie support.
>* 100% test coverage.
>* 100% type annotated codebase.
>* Few hard dependencies.

>[Middleware is used to apply logic with every request before it's processed by the view function.](https://www.google.com/search?qie=UTF-8)
[Middleware - an overview | ScienceDirect Topics ](https://www.sciencedirect.com/topics/computer-science/middleware)
>Middleware comprises the addition of a “middle” virtual layer between applications and the underlying platforms they run on. The layer is conceptually continuous across the entire system such that all processes sit above it and all platform resources are conceptually below it. By communicating through the layer, all aspects of location, the network, and computer boundaries are abstracted away
>Processes communicate only via the middleware layer; they are not concerned with physical aspects of the system such as which platform they are running on or the addresses of other processes they are communicating with. The virtual layer architecture of middleware provides significant transparency, in several of its forms, to processes.


[python - What problems can I solve with django middleware?](https://stackoverflow.com/questions/52460030/what-problems-can-i-solve-with-django-middleware/52460176)
>Middleware are actions that take place between server- and client-side interactions. Essentially they are just functions that are executed when a request is received by the server before and after the main server logic happens. They are useful if you have some action or check (or set of actions/checks) that needs to be performed on every or most requests.
>Authentication is a good example. You could perform an authentication check explicitly in every view function on your server, but that's not very DRY, it clutters the main logic of each view function, and what if you forget on a route? Instead, you can write a middleware that checks if the user is logged in. If they are, pass the request on a usual. If not, redirect them to the login page. Another example is Django's built-in CSRF protection middleware.
>It's not something like IBM's definition of middleware. Django's middleware is much smaller in scope and allows you to perform tasks in between a browser request and the business logic - or the other way around - in between the business logic and the response to the browser - or both. Typical tasks are:
>* Put information on the request object before it gets to the view (see AuthenticationMiddleware for an example)
>* Validate incoming requests
>* Add headers to responses
>* Intercept and reformat exceptions

>You can see middleware as a list of *implicit decorators* around every view. In short, middelware is thus used for *pre-processing requests*, and *post-processing responses*. It can also be used for example to perform *diagnostics* (measure the time between a request and a response).


[Concurrency and async / await - FastAPI ](https://fastapi.tiangolo.com/async/#in-a-hurry)
>If you are using third party libraries that tell you to call them with `await`, Then, declare your path operation functions with `async def`
>You can only use `await` inside of functions created with `async def`
>If you are using a third party library that communicates with something (a database, an API, the file system, etc) and doesn't have support for using `await`, (this is currently the case for most database libraries), then declare your path operation functions as normally, with just `def`
>you can mix `def` and `async def` in your path operation functions as much as you need and define each one using the best option for you. FastAPI will do the right thing with them. Anyway, in any of the cases above, FastAPI will still work asynchronously and be extremely fast

>Coroutine is just the very fancy term for the thing returned by an async def function. Python knows that it is something like a function that it can start and that it will end at some point, but that it might be paused ⏸ internally too, whenever there is an await inside of it.


[First Steps - FastAPI ](https://fastapi.tiangolo.com/tutorial/first-steps/)

>You can declare path "parameters" or "variables" with the same syntax used by Python format strings:
```py
@app.get("/items/{item_id}")
```


[FastAPI Tutorial - Building RESTful APIs with Python](https://www.youtube.com/watch?v=GN6ICac3OXY)


[Running FastAPI and celery together in a single command | by Davis Kirkendall | Level Up Coding ](https://levelup.gitconnected.com/running-fastapi-and-celery-together-in-a-single-command-66afd9b15561)
>Celery is probably the most used python library for running long running tasks within web applications.
>FastAPI and Celery are often used together (the FastAPI documentation even recommends this) and applications in spaces like data science and machine learning, where longer running *CPU bound tasks* need to be completed *asynchronously* are an ideal match for the combination of libraries.

>Speed of execution: FastAPI is async Capable. Thanks to Uvicorn and Starlette, the server and toolkit it is built upon. Flask doesn’t have that capability as of now (2020), so it gives the upper hand to FastAPI. Uvicorn uses Cython, as well as Pydantic, the library FastAPI uses for data validation. That allows FastAPI to perform faster and handle high concurrency than Flask. In some cases , it rivals in execution speed with Go and Javascript . (take this with a grain of salt, as YMMV).
>Plugins: This is where Flask wins. FastAPI currently lacks a plugin like Flask-Admin, that allows you to easily have a crud capabilty either for rapid scafoldding or end user interface for handling data. Though there is at least one in the making. (june 2020) FastAPI doesn’t have as mature plugins for User management as Flask has. But it is a matter of time for this issued to be addressed.

### FARM stack: FastAPI, React, and MongoDB!

[FARM Stack Course - FastAPI, React, MongoDB](https://www.youtube.com/watch?v=OzUzrs8uJl8)
[Learn the FARM Stack! (FastAPI, React, MongoDB) ](https://www.freecodecamp.org/news/learn-the-farm-stack-fastapi-reactjs-mongodb/)

FARP stack??
[FARP stack fastapi postgres](https://www.google.com/search?qsclient=gws-wiz)
[FARP Army meaning](https://www.google.com/search?qsadpr=1.41)
[Ordnance](https://en.wikipedia.org/wiki/Ordnance)

[Uvicorn ](https://www.uvicorn.org/)
[uvloop — uvloop Documentation ](https://uvloop.readthedocs.io/)

[FastAPI - The Good, the bad and the ugly. - DEV Community ](https://dev.to/fuadrafid/fastapi-the-good-the-bad-and-the-ugly-20ob)


### benchmarks

[Comparison with httptools · Issue #9 · python-hyper/h11 ](https://github.com/python-hyper/h11/issues/9)
[meinheld](https://www.google.com/search?qie=UTF-8)
[chi-gojay](https://www.google.com/search?qie=UTF-8)
[aah framework](https://www.google.com/search?qie=UTF-8)
[fastAPI benchmarks](https://www.google.com/search?qie=UTF-8)
[Benchmarks - FastAPI ](https://fastapi.tiangolo.com/benchmarks/)
[Bench-marking RESTful APIs ](https://gochronicles.com/benchmark-restful-apis/)

[FastAPI ](https://fastapi.tiangolo.com/#performance)
[Round 17 results - TechEmpower Framework Benchmarks ](https://www.techempower.com/benchmarks/#sectionhwtestl=zijmkf-1)
[Framework Benchmarks Round 17 - TechEmpower Blog ](https://www.techempower.com/blog/2018/10/30/framework-benchmarks-round-17/)
>Hauntingly High Performance. Break the curse of slow web-applications. Cleanse the vampiric drain of prematurely complex system architectures. Easily outrun the shambling zombies. High-performance is the treat you need this Halloween.

[FrameworkBenchmarks/flask-raw.dockerfile at master · TechEmpower/FrameworkBenchmarks ](https://github.com/TechEmpower/FrameworkBenchmarks/blob/master/frameworks/Python/flask/flask-raw.dockerfile)
[TechEmpower Framework Benchmarks ](https://www.techempower.com/benchmarks/#sectionrunidhwtestl=zijzen-7)

[How does Python's FastAPI compare to Node.js frameworks in terms of performance? ](https://www.quora.com/How-does-Pythons-FastAPI-compare-to-Node-js-frameworks-in-terms-of-performance)
>If you have a look at FastAPI benchmarks they pretend that it is on pair. Others benchmarks tends to give a slight advantage to Node.js frameworks. But there is a lot of node.js frameworks with some differences in terms of performance. Usually we are speaking about express.js. For FastAPI there is different configurations so we are speaking about the default one with Starlette. Overall, due to the fact that the benchmarks are far from real conditions, this type of difference is not significant. Both have asynchronous requests, what is the most important when it come to performance. They are not really multithread but you can launch several instances to occupy all the cores. *Your cache strategy is way more important than these tiny differences*. About the performance of langages themselves, node.js is based on Google Chrome JavaScript interpretor : V8. Python interpretor is less performant. But Python also has extremely performant data manipulation libraries written in low level languages. By the end the choice is not that linked to the performance of the frameworks. Python is more a language of choice for data manipulation and machine learning. Node.js’ based JavaScript is more a language of choice for classical apps.

>Meinheld is a high-performance WSGI-compliant web server that takes advantage of greenlet and picoev to enable asynchronous network I/O in a light-weight manner

according to [Web Frameworks Benchmark ](https://web-frameworks-benchmark.netlify.app/result?ascorder_by=level256), [Falcon](https://falconframework.org/) is the fastest Python framework, but still far behind other frameworks in Go, Java, Rust, C, JS, even PHP...
>P99 latency: The 99th latency percentile. This means 99% of requests will be faster than the given latency number. Put differently, only 1% of the requests will be slower than your P99 latency.

[falcon vs fastapi](https://www.google.com/search?qie=UTF-8)
[Flask vs Falcon vs FastAPI benchmark ](https://gist.github.com/nhymxu/814cf9b3294276629d2231248b709e26)
[Which api framework (Flask, DRF, Sanic, Falcon, FastAPI, Vibora, Starlette, etc) would you use today for a large team ? : Python ](https://www.reddit.com/r/Python/comments/c37w6j/which_api_framework_flask_drf_sanic_falcon/)
[Rewriting an API to Use FastAPI: Benchmarks and Lessons Learned ](https://andrewbrookins.com/python/is-fastapi-a-fad/)
>The inventor of FastAPI is Sebastián Ramírez. He’s a man with a fabulous mustache and an intense — some might say feverish — need to express himself with emojis.
>270 requests to 910 requests/second
>Migrating to FastAPI was not painless.
>I also liked using FastAPI, and it has supplanted Falcon as my “I need speed” Python framework.

[wrk linux](https://www.google.com/search?qie=UTF-8)
[wg/wrk: Modern HTTP benchmarking tool ](https://github.com/wg/wrk)
>wrk is a modern HTTP benchmarking tool capable of generating significant load when run on a single multi-core CPU. It combines a multithreaded design with scalable event notification systems such as epoll and kqueue.

[wrk for benchmarking and testing ](https://www.poppastring.com/blog/wrk-for-benchmarking-and-testing)
[How To Benchmark HTTP Latency with wrk on Ubuntu 14.04 | DigitalOcean ](https://www.digitalocean.com/community/tutorials/how-to-benchmark-http-latency-with-wrk-on-ubuntu-14-04)


### other

[AnyIO — AnyIO 3.5.0 documentation ](https://anyio.readthedocs.io/en/stable/)
[Coroutines and Tasks — Python 3.10.2 documentation ](https://docs.python.org/3/library/asyncio-task.html)
[Trio: a friendly Python library for async concurrency and I/O — Trio 0.19.0 documentation ](https://trio.readthedocs.io/en/stable/)
[Callback Hell ](http://callbackhell.com/)

RBAC - [Role-based access control](https://en.wikipedia.org/wiki/Role-based_access_control)


[leaky abstraction](https://www.google.com/search?qie=UTF-8)
[The Law of Leaky Abstractions – Joel on Software ](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)
[programming languages - Meaning of Leaky Abstraction?](https://stackoverflow.com/questions/3883006/meaning-of-leaky-abstraction)

[Dmitriy Kropivnitskiy's answer to Which is better, Flask or Django? ](https://www.quora.com/Which-is-better-Flask-or-Django/answer/Dmitriy-Kropivnitskiy)
>Django ORM sucks. ORMs suck in general, because no matter how hard the creators try to make them transparent they never are. It is a leaky abstraction. It pretends to remove the complexity of dealing with SQL and query optimization, but in reality once you go beyond the simplest queries you will have to deal with query performance and that means you have to know what the query is. And ORM will try its best not to tell you. And surprise-surprise, there is no way to replace Django ORM with anything. You can try to skip the model layer altogether, but that means you are not going to be able to use most of Django based libraries, because everything expects you to use models.


Fri 2022-02-18 17:19 / 00:19 ICT
email sent to

``Niyi <niyi@ncs-it.co.uk>, Kirk Jackson - Kitson Consulting <kirk@kitson-consulting.co.uk>, Geoffrey Ofori <g_ofori@hotmail.co.uk>, Mark Hadlich <mark@hadlich.co.uk>, Eugene Balkind <eugene.balkind.work@gmail.com>, James Kufre <kufre4ever@gmail.com>, Pete Donnell - Kitson Consulting <pete@kitson-consulting.co.uk>, John Sharp <xjh@hotmail.com>, Paul Jones <paul@slick360.co.uk>, Jonathan Howell <jon-howell@outlook.com>, Olivia Cheesbrough <oliviajcheesbrough@gmail.com>, David Longe <david@albistonbc.com>`

FastAPI

>C B <chrisjbird@gmail.com> 17:19 (0 minutes ago) to Niyi, Kirk, Geoffrey, Mark, Eugene, James, Pete, John, Paul, Jonathan, Olivia, `

Hi all,

As promised, here's my links and thoughts about FastAPI, an alternative to Flask which I'm looking into.

[FastAPI](https://fastapi.tiangolo.com/)

is a Python framework that is "high performance, easy to learn, fast to code, ready for production" (I bet they all say that...)

The main difference from Flask is that it uses asynchronous features of Python (`async` and `await`) that weren't available when Flask was developed, and when asynchronous programming was possible but very difficult to do. As web programming is mainly I/O bound and involves a lot of waiting around for various things to happen, it makes sense for a web framework to work asynchronously like NodeJS and Go frameworks do. It works with [ASGI](https://asgi.readthedocs.io/en/latest/), the Asynchronous Server Gateway Interface, which  is a "spiritual successor to WSGI",

The FastAPI website claims performance "on par with NodeJS and Go", - I'm not sure that's quite true, really, but it is one of the fastest Python frameworks, if not the fastest, and can be orders of magnitude faster than Flask depending on the kind of load.

Other features of FastAPI that set it apart from Flask are:

* Works with and includes [Uvicorn](https://www.uvicorn.org/), an ASGI web server that is supposedly production-ready (unlike Gunicorn, that a lot of people tend to use to develop Flask apps, and is considered definitely-not-production-ready so there are some bold warnings on the Flask website about not using it for production and hiding it behind a general-purpose web server like Apache, or usually Nginx, which then requires extra setup and introduces a performance hit)
* Has built-in support for Python [type hints](https://docs.python.org/3/library/typing.html) (though optional), via [Pydantic](https://pydantic-docs.helpmanual.io/) - and who doesn't love strong typing? ;)
* Has [authentication built in](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/), including Bearer auth, JWT, OAuth
* Has extensive [query validation](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/) features
* Has SwaggerUI built in (though that's easy to add to Flask), but also has a really nice-looking SwaggerUI alternative called [ReDoc](https://redocly.github.io/redoc/)
* Supports Dependency Injection (is that a good thing? Discuss...)

It's [apparently](https://towardsdatascience.com/build-and-host-fast-data-science-applications-using-fastapi-823be8a1d6a0) used by some big names including Netflix, Uber, and Microsoft and has [a lot of people](https://fastapi.tiangolo.com/fastapi-people/) working on it so should be pretty well-supported and maintained going forward.

Downsides?

* Well it's not Flask, if you're familiar with Flask, so will take some getting used to - though it is very similar to Flask
* Async programming might be a bit of a learning curve, though you don't have to do everything async, you can mix and match normal functions with `def` with async functions with `async def`
* [Someone said](https://www.infolytx.com/fast-api-gbu/) Request Validation is a bit of a pain
* [Someone else said](https://andrewbrookins.com/python/is-fastapi-a-fad/) that "Migrating to FastAPI was not painless."

But the general consensus seems to be that it's way faster than Flask, much more feature-complete, and easier to work with.

Let me know your thoughts!

Chris

