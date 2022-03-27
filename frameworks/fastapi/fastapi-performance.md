

/home/kvogel/projects/general/work/uhs/notes/220213-optimise-python.md

### FastAPI etc benchmarks article on Medium

asyncpg !
[FastAPI Microservice Patterns: GraphQL API | by Florian Kromer | Python in Plain English ](https://python.plainenglish.io/fastapi-microservice-patterns-graphql-api-b09ccb1de37f)

[FastAPI vs. Express.js vs. Flask vs. Nest.js Benchmark | by Travis Luong | Level Up Coding ](https://levelup.gitconnected.com/fastapi-vs-express-js-vs-flask-vs-nest-js-benchmark-5e14d518cc00)
>The winner is FastAPI + asyncpg + 4 gunicorn workers + ujson. FastAPI is definitely fast, on par with Node.js, and lives up to the hype! Well, according to these benchmarks. Just make sure you’re using the right libraries with it!
>Dmitriy Geels 2 months ago There is a huge flaw in your tests: running FastAPI with psycopg. The latter is synchronous which means it limits the throughput. Try another one - FastAPI + asyncpg to see the difference.
>Dean Lofts 2 months ago FastAPI is a beast.

[uvicorn workers](https://www.google.com/search?qsclient=gws-wiz)
[Settings - Uvicorn ](https://www.uvicorn.org/settings/)
[Server Workers - Gunicorn with Uvicorn - FastAPI ](https://fastapi.tiangolo.com/deployment/server-workers/)

[FastAPI vs. Fastify vs. Spring Boot vs. Gin Benchmark | by Travis Luong | Medium ](https://medium.com/@travisluong/fastapi-vs-fastify-vs-spring-boot-vs-gin-benchmark-b672a5c39d6c)
>In this article, I am pitting the champion, FastAPI, against a new set of faster competitors.
>Thomas Steinholz about 1 month ago (edited) The benchmarks should be using Starlette and Uvicorn for the FastAPI benchmark as they’re the (more performant) asynchronous counter part for Gunicorn

[travisluong/python-vs-nodejs-benchmark ](https://github.com/travisluong/python-vs-nodejs-benchmark)

[asyncpg — asyncpg Documentation ](https://magicstack.github.io/asyncpg/current/)
>asyncpg is a database interface library designed specifically for PostgreSQL and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL server binary protocol for use with Python’s asyncio framework.

