
[Pipenv: A Guide to the New Python Packaging Tool – Real Python ](https://realpython.com/pipenv-guide/)
>“How do you allow for deterministic builds for your Python project without gaining the responsibility of updating versions of sub-dependencies?”
>Spoiler alert: The easy answer is using Pipenv.







[python - How are Pipfile and Pipfile.lock used?](https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used)
>`Pipfile` is the dedicated file used by the Pipenv virtual environment to manage project dependencies. 

### Install

```
21/02/1 16:23:45 kvogel-elitebook:~/p/primrose/kilo ±(master)
❯ pipenv
zsh: command not found: pipenv
❯ python -m pipenv
/usr/bin/python: No module named pipenv

21/02/1 16:26:43 kvogel-elitebook:~/p/primrose/kilo ±(master)
❯ pip3 install pipenv
Collecting pipenv
  Downloading pipenv-2020.11.15-py2.py3-none-any.whl (3.9 MB)
Collecting virtualenv
  Downloading virtualenv-20.4.2-py2.py3-none-any.whl (7.2 MB)
Collecting virtualenv-clone>=0.2.5
  Downloading virtualenv_clone-0.5.4-py2.py3-none-any.whl (6.6 kB)
Requirement already satisfied: pip>=18.0 in /usr/lib/python3/dist-packages (from pipenv) (20.0.2)
Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from pipenv) (2019.11.28)
Requirement already satisfied: setuptools>=36.2.1 in /usr/lib/python3/dist-packages (from pipenv) (45.2.0)
Requirement already satisfied: six<2,>=1.9.0 in /usr/lib/python3/dist-packages (from virtualenv->pipenv) (1.14.0)
Collecting filelock<4,>=3.0.0
  Downloading filelock-3.0.12-py3-none-any.whl (7.6 kB)
Collecting distlib<1,>=0.3.1
  Downloading distlib-0.3.1-py2.py3-none-any.whl (335 kB)
Collecting appdirs<2,>=1.4.3
  Downloading appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
Installing collected packages: filelock, distlib, appdirs, virtualenv, virtualenv-clone, pipenv
  WARNING: The script virtualenv is installed in '/home/kvogel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script virtualenv-clone is installed in '/home/kvogel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts pipenv and pipenv-resolver are installed in '/home/kvogel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed appdirs-1.4.4 distlib-0.3.1 filelock-3.0.12 pipenv-2020.11.15 virtualenv-20.4.2 virtualenv-clone-0.5.4
21/02/1 16:29:12 kvogel-elitebook:~/p/primrose/kilo ±(master)
❯ which pipenv
pipenv not found
```
> `WARNING: The scripts pipenv and pipenv-resolver are installed in '/home/kvogel/.local/bin' which is not on PATH.`
```
21/02/2 2:52:42 kvogel-elitebook:~/projects/primrose ±(master) ✗ 
❯ ls ~/.local/bin              
mako-render*  markdown2*  markdown_py*  pdoc*  pdoc3*  pipenv*  pipenv-resolver*  virtualenv*  virtualenv-clone*
❯ vi ~/.zshrc
```
```diff
+export PATH=$PATH:~/.local/bin
```
```    
❯ . ~/.zshrc 
❯ which pipenv
/home/kvogel/.local/bin/pipenv
```


