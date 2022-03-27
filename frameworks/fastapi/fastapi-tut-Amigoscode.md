
### [FastAPI Tutorial - Building RESTful APIs with Python](https://www.youtube.com/watch?v=GN6ICac3OXY) notes

[RESTful](file:///home/kvogel/projects/general/dev/arch/REST/RESTful.md) [HTTP verbs](file:///home/kvogel/projects/general/dev/arch/REST/http-verbs.md)


```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"Hello": "Async"}
```

[async await](https://youtu.be/GN6ICac3OXY?t=910)


`models.py`
Pydantic

```py
from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
  male = "male"
  female = "female"

class User(BaseModel):
  id: Optional[UUID] = uuid4
  first_name: str
  last_name: str
  middle_name: Optional[str]
  gender: Gender
  roles=
```
>pydantic is a library to perform data validation, we can declare the shape of our data as classes with attributes

["database"](https://youtu.be/GN6ICac3OXY?t=1294)


Thu 2022-02-24 17:16 / 00:16 ICT
```py
# "database"
db: List[User] = [
    User(id=uuid4(), first_name="Christopher", middle_name="John", last_name="Bird", gender=Gender.male, roles=[Role.user]),
    # ...
]

@app.get("/users")
async def fetch_users():
  return db
```

http://127.0.0.1:8000/users
```json
[{"id":"7e249d0f-a166-4415-9ee3-ef005f8537a1","first_name":"Christopher","middle_name":"John","last_name":"Bird","gender":"male","roles":["user"]},{"id":"e6ae85e7-2459-49cb-bdb2-d8c09e385a8e","first_name":"Kevin","middle_name":null,"last_name":"Smith","gender":"male","roles":["admin"]}]
```

Thu 2022-02-24 17:25 / 00:25 ICT
[post requests](https://youtu.be/GN6ICac3OXY?t=1914)

[Thunder Client](https://youtu.be/GN6ICac3OXY?t=1988)

[thunder client](file:///home/kvogel/projects/general/dev/apps/vscode/extensions/thunder-client.md) - installed already, enabled in workspace


```
2022-02-25 06:19:12 kvogel@kvogel-surface-ubuntu:~
❯ curl -X MUX -i  http://127.0.0.1:8000
curl: (52) Empty reply from server
2022-02-25 06:19:22 kvogel@kvogel-surface-ubuntu:~
```


## done


### demo setup

setup python venv
```
2022-02-24 14:40:35 kvogel@kvogel-surface-ubuntu:~/projects/general/dev/learn/python/frameworks/fastapi/demo ±(master) ✗
❯ python3 -m venv venv
❯ . ./venv/bin/activate
(venv) 2022-02-24 14:41:06 kvogel@kvogel-surface-ubuntu:~/projects/general/dev/learn/python/frameworks/fastapi/demo ±(master) ✗
❯ which python
/home/kvogel/projects/general/dev/learn/python/frameworks/fastapi/demo/venv/bin/python
❯ python -V
Python 3.10.2
```
install FastAPI and other supporting packages:
```
(venv) 2022-02-24 14:41:15 kvogel@kvogel-surface-ubuntu:~/projects/general/dev/learn/python/frameworks/fastapi/demo ±(master) ✗
❯ pip install "fastapi[all]"
...
Successfully installed MarkupSafe-2.1.0 anyio-3.5.0 asgiref-3.5.0 certifi-2021.10.8 charset-normalizer-2.0.12 click-8.0.4 dnspython-2.2.0 email-validator-1.1.3 fastapi-0.74.1 h11-0.13.0 httptools-0.2.0 idna-3.3 itsdangerous-2.1.0 jinja2-3.0.3 orjson-3.6.7 pydantic-1.9.0 python-dotenv-0.19.2 python-multipart-0.0.5 pyyaml-5.4.1 requests-2.27.1 six-1.16.0 sniffio-1.2.0 starlette-0.17.1 typing-extensions-4.1.1 ujson-4.3.0 urllib3-1.26.8 uvicorn-0.15.0 uvloop-0.16.0 watchgod-0.7 websockets-10.2
```


### Error via HTTPS

bc calling via https, and https not implemented yet!

`GET https://localhost:8000/users`:
```
WARNING:  Invalid HTTP request received.
Traceback (most recent call last):
  File "/home/kvogel/projects/general/dev/learn/python/frameworks/fastapi/demo/venv/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 131, in data_received
    self.parser.feed_data(data)
  File "httptools/parser/parser.pyx", line 212, in httptools.parser.parser.HttpParser.feed_data
httptools.parser.errors.HttpParserInvalidMethodError: Invalid method encountered
```

`GET http://localhost:8000/users`:
```
INFO:     127.0.0.1:46098 - "GET /users HTTP/1.1" 200 OK
```

[Catch `HttpParserInvalidMethodError` exception · Issue #75 · encode/uvicorn ](https://github.com/encode/uvicorn/issues/75)
[Handle exception when receive request with custom method · Issue #1296 · encode/uvicorn ](https://github.com/encode/uvicorn/issues/1296)
[python - Invalid HTTP method in Traceback: Uvicorn](https://stackoverflow.com/questions/65878595/invalid-http-method-in-traceback-uvicorn)
>I was getting the same arcane WARNING:  Invalid HTTP request received. error with an unhelpful stack trace. I tried all of the environment variable tweaks recommended and none worked (see FastAPI issue #680, uvicorn issue #441).
>My issue was that when I was calling my FastAPI microservice I was using https when my microservice did not have HTTPS support. I changed the url from https to http and it started working as expected.

[Status 502: [WARNING] Invalid HTTP request received. · Issue #680 · tiangolo/fastapi ](https://github.com/tiangolo/fastapi/issues/680#issuecomment-621365894)
[Stuck with: WARNING: Invalid HTTP request received. · Issue #441 · encode/uvicorn ](https://github.com/encode/uvicorn/issues/441#issuecomment-610542388)
