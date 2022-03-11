
this: [Developing and Testing an Asynchronous API with FastAPI and Pytest | TestDriven.io ](https://testdriven.io/blog/fastapi-crud/)

>By the end of this tutorial you should be able to:
>* Develop an asynchronous RESTful API with Python and FastAPI
>* Practice Test-driven Development
>* Test a FastAPI app with pytest
>* Interact with a Postgres database asynchronously
>* Containerize FastAPI and Postgres inside a Docker container
>* Parameterize test functions and mock functionality in tests with pytest
>* Document a RESTful API with Swagger/OpenAPI


```
(venv) 2022-03-03 07:31:57 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3 ±(main) ✗
❯ sudo docker-compose up -d --build
```

http://localhost:8002/ping
```json
{"ping":"pong!"}
```



hot reloads even inside container - added route to source (`main.py`) of running container:
```py
@app.get("/hello")
def pong():
    return {"hello": "Hello, World!"}
```
then went to http://localhost:8002/hello :
```json
{"hello":"Hello, World!"}
```
404: http://localhost:8002/helloasdfs
```json
{"detail":"Not Found"}
```

To run tests:
```
# docker-compose exec web pytest
```

```
2022-03-03 08:34:24 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3 ±(main) ✗
❯ sudo docker-compose exec web pytest
================================================================================ test session starts =================================================================================
platform linux -- Python 3.9.4, pytest-6.2.3, py-1.11.0, pluggy-0.13.1
rootdir: /usr/src/app
plugins: anyio-3.5.0
collected 1 item

tests/test_main.py .                                                                                                                                                           [100%]

================================================================================= 1 passed in 0.27s ==================================================================================
```

>Fixture. A particular environment that must be set up before a test can be run.

### Async

>As long as you don't have any blocking I/O calls in the handler, you can simply declare the handler as asynchronous by adding the async keyword like so:


### Routes

>For each route, we'll:
>* write a test
>* run the test, to ensure it fails (red)
>* write just enough code to get the test to pass (green)
>* refactor (if necessary)

>You can break up and modularize larger projects as well as apply versioning to your API with the *APIRouter*.
>If you're familiar with Flask, it is *equivalent to a Blueprint*.

