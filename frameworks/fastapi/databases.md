

### `encode/databases`

What a dumb name...

[Databases ](https://www.encode.io/databases/)
```
(venv) 2022-03-27 19:05:58 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ pip freeze | diff requirements.txt -
```
```diff
2c2
< arrow
---
> arrow==1.2.1
46c46
< typing-extensions==4.1.1
---
> typing_extensions==4.1.1
```
??

```
(venv) 2022-03-27 19:06:14 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ pip install databases
❯ pip install "databases[postgresql]"
Successfully installed asyncpg-0.25.0
❯ pip freeze | diff requirements.txt -
```
```diff
2c2
< arrow
---
> arrow==1.2.1
3a4
> asyncpg==0.25.0
9a11
> databases==0.5.5
16a19
> greenlet==1.1.2
42a46
> SQLAlchemy==1.4.32
46c50
< typing-extensions==4.1.1
---
> typing_extensions==4.1.1
```
```
❯ pip freeze > requirements.txt
```
[Databases ](https://www.encode.io/databases/)
[encode/databases: Async database support for Python. 🗄 ](https://github.com/encode/databases/)

[Python databases](https://www.google.com/search?q=Python+databases)
[fastapi databases](https://www.google.com/search?q=fastapi+databases)
[Python encode databases](https://www.google.com/search?q=Python+encode+databases)

[Encode ](https://github.com/encode)
[Projects - Encode ](https://www.encode.io/projects/)

Submitted an issue about the name: [Name change? · Issue #479 · encode/databases ](https://github.com/encode/databases/issues/479)

