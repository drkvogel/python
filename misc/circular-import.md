

`ImportError` on `flask run`? run `python lims.py`
>Running the command `python app.py` will help you to know exactly when the `ImportError` happens.

search `ImportError: cannot import name from partially initialized module (most likely due to a circular import)`
[ImportError: cannot import name from partially initialized module (most likely due to a circular import)](https://www.google.com/search?qie=UTF-8)
[python - ImportError: cannot import name '...' from partially initialized module '...' (most likely due to a circular import)](https://stackoverflow.com/questions/64807163/importerror-cannot-import-name-from-partially-initialized-module-m)
[Circular (or cyclic) imports in Python](https://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python)
[flask circular imports](https://www.google.com/search?qie=UTF-8)
[python - Can I avoid circular imports in Flask and SQLAlchemy](https://stackoverflow.com/questions/42909816/can-i-avoid-circular-imports-in-flask-and-sqlalchemy)
[cookiecutter-flask/cookiecutter-flask: A flask template with Bootstrap 4, asset bundling+minification with webpack, starter templates, and registration/authentication. For use with cookiecutter. ](https://github.com/cookiecutter-flask/cookiecutter-flask)
[Application Factories — Flask Documentation (2.0.x) ](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/)
[cookiecutter-flask/app.py at master · cookiecutter-flask/cookiecutter-flask ](https://github.com/cookiecutter-flask/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py#L26)
[TTWShell/hobbit-core: A flask project generator. ](https://github.com/TTWShell/hobbit-core)
[Web-Apps on Flask: How to Deal With Cyclic Imports - CodeProject ](https://www.codeproject.com/Articles/5265893/Web-Apps-on-Flask-How-to-Deal-With-Cyclic-Imports)
[Flask web applications: how to deal with cyclic imports - Prog.World ](https://prog.world/flask-web-applications-how-to-deal-with-cyclic-imports/)

[python - Can I avoid circular imports in Flask and SQLAlchemy](https://stackoverflow.com/questions/42909816/can-i-avoid-circular-imports-in-flask-and-sqlalchemy/51739367#51739367)


`/home/kvogel/projects/general/work/uhs/repos/chilworth_wms/data-api/app.py`:
```py
# following section adapted from https://stackoverflow.com/a/51739367
# it's necessary to avoid circular dependencies on the db object
def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
```


```
(venv) 2022-02-16 09:24:47 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/backend ±(master) ✗ 
❯ ./run debug
executing 'python lims.py'
Traceback (most recent call last):
  File "lims.py", line 1, in <module>
    from app import app
  File "/home/kvogel/projects/general/work/uhs/v3/backend/app/__init__.py", line 17, in <module>
    from app import routes
  File "/home/kvogel/projects/general/work/uhs/v3/backend/app/routes.py", line 19, in <module>
    db = SQLAlchemy(app)
  File "/home/kvogel/projects/general/work/uhs/v3/backend/venv/lib/python3.8/site-packages/flask_sqlalchemy/__init__.py", line 761, in __init__
    self.init_app(app)
  File "/home/kvogel/projects/general/work/uhs/v3/backend/venv/lib/python3.8/site-packages/flask_sqlalchemy/__init__.py", line 848, in init_app
    'SQLALCHEMY_DATABASE_URI' not in app.config and
AttributeError: partially initialized module 'app' has no attribute 'config' (most likely due to a circular import)
```

