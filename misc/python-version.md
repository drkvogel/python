
### Python version

In the FastAPI docs, e.g. [Path Parameters and Numeric Validations - FastAPI ](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/), many examples have
"Python 3.6 and above" and "Python 3.10 and above" code samples

currently have 3.8.10:
```
(venv) 2022-02-21 09:56:09 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3 ±(master)
❯ python -V
Python 3.8.10
❯ python3 -V
Python 3.8.10
```
but why? bc default for my Ubuntu version:
```
2022-02-21 10:02:35 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs ±(master) ✗
❯ cat /etc/lsb-release | clipcopy
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.3 LTS"
```
>Python 3.8
>In 20.04 LTS, the python included in the base system is Python 3.8.

FastAPI is for 3.6+:
>FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

let's stick on the <3.10 examples for now...

Wed 2022-02-23 08:15 / 15:15 ICT
but... then can't use funky new syntax in FastAPI! And would be good to learn...

[virtualenv - python3 -m venv: how to specify Python point release/version?](https://stackoverflow.com/questions/54700307/python3-m-venv-how-to-specify-python-point-release-version)
>`python3.6 -m venv whatever`

used [asdf](file:///home/kvogel/projects/general/dev/apps/asdf.md) to install Python 3.10.2


### python version in venv is 3.8, not 3.10!

```
(venv) 2022-03-24 12:28:22 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main) ✗
❯ python -V
Python 3.8.10
❯ which python
/home/kvogel/projects/general/work/uhs/v3/fastapi/venv/bin/python
```
outside venv:
```
2022-03-24 10:48:00 kvogel@kvogel-surface-ubuntu:~/projects
❯ python -V
Python 3.10.2
❯ which python
/home/kvogel/.asdf/shims/python
```
notes/220221-python-version.md
>[virtualenv - python3 -m venv: how to specify Python point release/version?](https://stackoverflow.com/questions/54700307/python3-m-venv-how-to-specify-python-point-release-version)
>`python3.6 -m venv whatever`
>used [asdf](file:///home/kvogel/projects/general/dev/apps/asdf.md) to install Python 3.10.2

>Since Python 3, the Python Docs suggest creating the virtual environment with the following command: `python3 -m venv <myenvname>`.
>*Please note that venv does not permit creating virtual environments with other versions of Python*. For that, install and use the virtualenv package.

doh, somehow I've created a venv with py3.8...

check can create venv with py3.10 from asdf:
```
2022-03-24 12:43:38 kvogel@kvogel-surface-ubuntu:~/projects/tmp
❯ python -V
Python 3.10.2
❯ python -m venv venv
❯ . ./venv/bin/activate
(venv) 2022-03-24 12:44:15 kvogel@kvogel-surface-ubuntu:~/projects/tmp
❯ python -V
Python 3.10.2
❯ which python
/home/kvogel/projects/tmp/venv/bin/python
```
OK
can I upgrade in the venv?? Or do I have to recreate? sure I've been through this before...
`python3 -m venv --upgrade`?
```
(venv) 2022-03-24 12:49:01 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ python3 -m venv --upgrade venv
❯ python -V
Python 3.8.10
❯ deactivate
2022-03-24 12:49:49 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ . ./venv/bin/activate
(venv) 2022-03-24 12:49:53 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ python -V
Python 3.8.10
```
no dice
```
2022-03-24 12:59:10 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ python -m venv --upgrade venv
2022-03-24 12:59:17 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ . ./venv/bin/activate
(venv) 2022-03-24 12:59:22 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ python -V
Python 3.8.10
(venv) 2022-03-24 12:59:29 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ pip freeze | diff requirements.txt -
```
```diff
2c2
< arrow
---
> arrow==1.2.2
```

```
(venv) 2022-03-24 14:47:57 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ deactivate
2022-03-24 14:48:09 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ mv venv venv3.8
❯ python -V
Python 3.10.2
❯ python -m venv venv
❯ ./venv/bin/activate
❯ ./venv/bin/python -V
Python 3.10.2
❯ . ./venv/bin/activate
(venv) 2022-03-24 15:27:55 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ python -V
Python 3.10.2
```
oorah. thought I'd sorted that before!
```
(venv) 2022-03-24 15:30:09 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ pip install < requirements.txt
ERROR: You must give at least one requirement to install (see "pip help install")
WARNING: You are using pip version 21.2.4; however, version 22.0.4 is available.
You should consider upgrading via the '/home/kvogel/projects/general/work/uhs/v3/fastapi/venv/bin/python -m pip install --upgrade pip' command.
(venv) 2022-03-24 15:30:37 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main)
❯ python -m pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.10/site-packages (21.2.4)
...
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-22.0.4

❯ pip install -r requirements.txt
```

