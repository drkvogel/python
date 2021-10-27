

```
2021-06-18 01:22:01 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗ 
❯ python --version
Python 2.7.18
❯ python3 --version
Python 3.8.5
❯ python3 -m venv venv
❯ . ./venv/bin/activate
❯ pip install Django
Collecting Django
  Downloading Django-3.2.4-py3-none-any.whl (7.9 MB)
Successfully installed Django-3.2.4 asgiref-3.3.4 pytz-2021.1 sqlparse-0.4.1
(venv) 2021-06-18 01:33:35 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗
❯ python -V
Python 3.8.5
(venv) 2021-06-18 01:33:41 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗
❯ python
Python 3.8.5 (default, May 27 2021, 13:30:53)
>>> import django
>>> dir(django)
['VERSION', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'get_version', 'setup', 'utils']
>>> django.VERSION
(3, 2, 4, 'final', 0)
```
or with `bpython` now aliased as `bp`:
```
(venv) 2021-06-18 01:53:36 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗
❯ bp
bpython version 0.21 on top of Python 3.8.5 /home/kvogel/projects/general/dev/learn/python/frameworks/django/drf/venv/bin/python3
>>> import django
>>> print(django.get_version())
3.2.4
```
or:
```
(venv) 2021-06-18 01:56:07 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗
❯ python -m django --version
3.2.4
```

```
(venv) 2021-06-18 01:57:17 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗
❯ django-admin startproject drf-test
CommandError: 'drf-test' is not a valid project name. Please make sure the name is a valid identifier.
(venv) 2021-06-18 01:57:29 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗
❯ django-admin startproject drftest
```

[Quickstart - Django REST framework ](https://www.django-rest-framework.org/tutorial/quickstart/)

install djangorestframework:
```
(venv) 2021-06-18 01:57:38 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf ±(master) ✗
❯ pip install djangorestframework
...
Successfully installed djangorestframework-3.12.4
```

sync db:
```
(venv) 2021-06-18 01:59:22 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf/drftest ±(master) ✗
❯ python manage.py migrate
```
create admin user:
```
(venv) 2021-06-18 02:00:34 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf/drftest ±(master) ✗
❯ python manage.py createsuperuser --email chrisjbird@gmail.com --username admin
Password: password123
Password (again):
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

create app in project:
```
(venv) 2021-06-18 02:02:46 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf/drftest ±(master) ✗ 
❯ django-admin startapp quickstart
❯ ls
db.sqlite3  drftest/  manage.py*  quickstart/
❯ ls drftest 
__init__.py  __pycache__/  asgi.py  settings.py  urls.py  wsgi.py
❯ ls quickstart 
__init__.py  admin.py  apps.py  migrations/  models.py  tests.py  views.py
```
check migrate again:
```
(venv) 2021-06-18 02:01:24 kvogel-surface:~/projects/general/dev/learn/python/frameworks/django/drf/drftest ±(master) ✗
❯ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

created `frameworks/django/drf/drftest/quickstart/serializers..py`

>Notice that we're using hyperlinked relations in this case with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design.


>Extension activation failed, run the 'Developer: Toggle Developer Tools' command for more information.
>Source: Jupyter (Extension)

```
console.ts:137 [Extension Host] extension activation failed TypeError: Cannot read property 'packageJSON' of undefined
	at /home/kvogel/.vscode-server/extensions/ms-toolsai.jupyter-2021.6.999406279/out/client/extension.js:1:99089
	at f (/home/kvogel/.vscode-server/extensions/ms-toolsai.jupyter-2021.6.999406279/out/client/extension.js:1:99167)
	at Object.p [as sendTelemetryEvent] (/home/kvogel/.vscode-server/extensions/ms-toolsai.jupyter-2021.6.999406279/out/client/extension.js:1:98937)
	at t.ExperimentationTelemetry.postEvent (/home/kvogel/.vscode-server/extensions/ms-toolsai.jupyter-2021.6.999406279/out/client/extension.js:52:717910)
	at s.PostEventToTelemetry (/home/kvogel/.vscode-server/extensions/ms-toolsai.jupyter-2021.6.999406279/out/client/extension.js:52:716314)
	at s.isCachedFlightEnabled (/home/kvogel/.vscode-server/extensions/ms-toolsai.jupyter-2021.6.999406279/out/client/extension.js:52:715725)
S @ console.ts:137
mainThreadExtensionService.ts:95 Activating extension 'ms-python.python' failed: Cannot read property 'packageJSON' of undefined.
$onExtensionActivationError @ mainThreadExtensionService.ts:95
mainThreadExtensionService.ts:95 Cannot activate unknown extension 'ms-python.vscode-pylance'
```

[python - What exactly do "u" and "r" string flags do, and what are raw string literals?](https://stackoverflow.com/questions/2081640/what-exactly-do-u-and-r-string-flags-do-and-what-are-raw-string-literals)

frameworks/django/drf/drftest/drftest/urls.py

think I've created the app - `quickstart` at the wrong level, should be inside the *project* `drftest`?
