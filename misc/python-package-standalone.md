


search `pyinstall`

tried to do for [covfefe](/projects/repos/covfefe/notes/covfefe-cli.md)

fuck asdf and use pyenv, or brew python?? or poetry?

[how to package a python application into a single command](https://www.google.com/search?q=how+to+package+a+python+application+into+a+single+command&ie=UTF-8)
[How do I package a single python script which takes command line arguments and also has dependencies?](https://stackoverflow.com/questions/55271050/how-do-i-package-a-single-python-script-which-takes-command-line-arguments-and-a)
[How can I make a Python script standalone executable to run without ANY dependency?](https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen)
[compilation - Create a single executable from a Python project](https://stackoverflow.com/questions/12059509/create-a-single-executable-from-a-python-project)


>There are several different ways of doing this. The first -- and likely most common -- way is to use "freeze" style programs. These programs work by bundling together Python and your program, essentially combining them into a single executable:
>PyInstaller: Website || Repo || PyPi Supports Python 3.7 - 3.10 on Windows, Mac, and Linux.
>cx_Freeze: Website || Repo || PyPi Supports Python 3.6 - 3.10 on Windows, Mac, and Linux.
>py2exe: Website || Repo || PyPi Supports Python 3.7 - 3.10 on Windows only.
>py2app: Website || Repo || PyPi Supports Python 3.6 - 3.10 on Macs only.


[PyInstaller Manual — PyInstaller 5.11.0 documentation ](https://pyinstaller.org/en/stable/)
[Nuitka the Python Compiler — Nuitka the Python Compiler documentation ](https://nuitka.net/)
[packaging - How to package a Python project to be run in the console](https://stackoverflow.com/questions/69638969/how-to-package-a-python-project-to-be-run-in-the-console)
[The pyproject.toml file  Documentation  Poetry - Python dependency management and packaging made easy ](https://python-poetry.org/docs/pyproject/#scripts)
[flit/pyproject.toml at 96751efce651f8bae8ccb9e7f144dac460b3f013 · pypa/flit ](https://github.com/pypa/flit/blob/96751efce651f8bae8ccb9e7f144dac460b3f013/pyproject.toml#L43-L44)

### Pyinstaller

```
23/05/27 14:26:58 kvogel@kvogel-macbook-2021:~
❯ pip install pyinstaller

(venv) 23/05/27 14:27:18 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ pyinstaller ocr.py
...
OSError: Python library not found: libpython3.11.dylib, libpython3.11m.dylib, .Python, Python, Python3
    This means your Python installation does not come with proper shared library files.
    This usually happens due to missing development package, or unsuitable build parameters of the Python installation.

    * On Debian/Ubuntu, you need to install Python development packages:
      * apt-get install python3-dev
      * apt-get install python-dev
    * If you are building Python by yourself, rebuild with `--enable-shared` (or, `--enable-framework` on macOS).
    *
(venv) 23/05/27 14:27:34 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ deactivate
23/05/27 14:27:54 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ pyinstaller ocr.py
119 INFO: PyInstaller: 5.11.0
119 INFO: Python: 3.11.0
128 INFO: Platform: macOS-13.2.1-arm64-arm-64bit
128 INFO: wrote /Users/kvogel/projects/ocr/ocr.spec



OSError: Python library not found: libpython3.11m.dylib, Python3, libpython3.11.dylib, .Python, Python
    This means your Python installation does not come with proper shared library files.
    This usually happens due to missing development package, or unsuitable build parameters of the Python installation.

    * On Debian/Ubuntu, you need to install Python development packages:
      * apt-get install python3-dev
      * apt-get install python-dev
    * If you are building Python by yourself, rebuild with `--enable-shared` (or, `--enable-framework` on macOS).
    *
```


```
23/05/27 14:33:51 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ which -a python
/Users/kvogel/.asdf/shims/python

23/05/27 14:33:56 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ brew install python
Warning: python@3.11 3.11.3 is already installed and up-to-date.
To reinstall 3.11.3, run:
  brew reinstall python@3.11
23/05/27 14:34:28 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ brew reinstall python
...
==> Reinstalling python@3.11
==> Pouring python@3.11--3.11.3.arm64_ventura.bottle.tar.gz
==> /opt/homebrew/Cellar/python@3.11/3.11.3/bin/python3.11 -m ensurepip
==> /opt/homebrew/Cellar/python@3.11/3.11.3/bin/python3.11 -m pip install -v --no-deps --no-index --upgrad
🍺  /opt/homebrew/Cellar/python@3.11/3.11.3: 3,178 files, 62.1MB
==> Running `brew cleanup python@3.11`...
...

❯ /opt/homebrew/Cellar/python@3.11/3.11.3/bin/python3
Python 3.11.3 (main, Apr  7 2023, 20:13:31) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Not in PATH?
[homebrew - How do I use brew installed Python as the default Python?](https://stackoverflow.com/questions/5157678/how-do-i-use-brew-installed-python-as-the-default-python)

>For Apple Silicon machines, the path are slightly different. After running brew install python, you must ensure your `~/.zshrc` uses the correct Homebrew paths:

```
23/05/27 14:38:21 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ which -a python3
/Users/kvogel/.asdf/shims/python3
/opt/homebrew/bin/python3
/usr/bin/python3
```

[pyinstaller error: OSError: Python library not found: libpython3.4mu.so.1.0, libpython3.4m.so.1.0, libpython3.4.so.1.0](https://stackoverflow.com/questions/43067039/pyinstaller-error-oserror-python-library-not-found-libpython3-4mu-so-1-0-lib)
>for Linux system like your CentOS, try rebuild python to generated shared lib using: `env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.4.4` as said in pyenv offical doc
>Thank you -- this was a bit hard to find in the docs / wiki directly but it is what *made it work for me on macOS*. – Taylor D. Edmiston Jan 23, 2020 at 22:29

`PYTHON_CONFIGURE_OPTS="--enable-shared"`? no dice.
```
23/05/27 14:39:50 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ env PYTHON_CONFIGURE_OPTS="--enable-shared" pyinstaller ocr.py
```

ah, but they mean *install Python* with that envvar - e.g. with `pyenv` as they've done, but mine is installed via asdf


[How to reinstall already installed toolchains · Issue #34 · asdf-vm/asdf ](https://github.com/asdf-vm/asdf/issues/34)
```
asdf uninstall $plug $v
asdf install $plug $v
```

```
23/05/27 14:54:09 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ asdf uninstall python
❯ which -a python
/Users/kvogel/.asdf/shims/python
❯ which -a python3
/Users/kvogel/.asdf/shims/python3
/opt/homebrew/bin/python3
/usr/bin/python3
```
que??

```
23/05/27 14:59:55 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ asdf current
nodejs          19.0.1          /Users/kvogel/.tool-versions
python          3.11.0          Not installed. Run "asdf install python 3.11.0"

23/05/27 15:02:24 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ python
No python executable found for python 3.11.0

23/05/27 15:02:54 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ which -a python3
/Users/kvogel/.asdf/shims/python3
/opt/homebrew/bin/python3
/usr/bin/python3
23/05/27 15:02:58 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ /Users/kvogel/.asdf/shims/python3
Python 3.11.3 (main, Apr  7 2023, 20:13:31) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ^D

```
???


where is pyinstaller installed now?

```
23/05/27 15:03:16 kvogel@kvogel-macbook-2021:~/projects/ocr
❯ which -a pyinstaller
/Users/kvogel/.asdf/shims/pyinstaller
```
so pyinstaller was installed to the asdf env, which doesn't have the dev libs...

oh, this is too much, now, and low low priority...
lets put this folder under general.git so I can reference it for later




[OSError: Python library not found: libpython3.11.dylib](https://www.google.com/search?q=OSError%3A+Python+library+not+found%3A+libpython3.11.dylib&ie=UTF-8)
[virtualenv - getting os error python library not found](https://stackoverflow.com/questions/65569706/getting-os-error-python-library-not-found)
[python - pyinstaller causes OSerror](https://stackoverflow.com/questions/68380129/pyinstaller-causes-oserror)
[pyinstaller error: OSError: Python library not found: libpython3.4mu.so.1.0, libpython3.4m.so.1.0, libpython3.4.so.1.0](https://stackoverflow.com/questions/43067039/pyinstaller-error-oserror-python-library-not-found-libpython3-4mu-so-1-0-lib)
[Linking to system python lib fails…  Apple Developer Forums ](https://developer.apple.com/forums/thread/696281)
[Pyinstaller: OSError: Python library not found](https://stackoverflow.com/questions/68583709/pyinstaller-oserror-python-library-not-found)
[OSError: Python library not found: libpython3.9mu.so.1.0, libpython3.9m.so, etc., when running pyinstaller](https://stackoverflow.com/questions/68462920/oserror-python-library-not-found-libpython3-9mu-so-1-0-libpython3-9m-so-etc)
[macos python-dev](https://www.google.com/search?q=macos+python-dev&ie=UTF-8)
[macos - how to install python-devel in Mac OS?](https://stackoverflow.com/questions/32578106/how-to-install-python-devel-in-mac-os)
[django - Can't find a way to install python-dev on Mac OS X](https://stackoverflow.com/questions/33843313/cant-find-a-way-to-install-python-dev-on-mac-os-x)
[macos - How to install the Python development headers on Mac OS X?](https://stackoverflow.com/questions/15931331/how-to-install-the-python-development-headers-on-mac-os-x)
[Issues installing Python 3.8.10 on macOS 12.3 Monterey](https://stackoverflow.com/questions/71577626/issues-installing-python-3-8-10-on-macos-12-3-monterey)
[Installing Python 3.x dev environment on MacOS the right way and automating new project setup using Automator  by J Vats  Geek Culture  Medium ](https://medium.com/geekculture/installing-python-3-x-development-environment-on-macos-a64c0141b20c)
[Python Dev Setup for (M1) Macs ](https://gist.github.com/cgons/d4e1d7c7f0f4e7e2de173852729fb2cc)
[asdf python-devel](https://www.google.com/search?q=asdf+python-devel&ie=UTF-8)
[Python development headers · Issue #117 · asdf-community/asdf-python ](https://github.com/asdf-community/asdf-python/issues/117)
[pyenv/plugins/python-build at master · pyenv/pyenv ](https://github.com/pyenv/pyenv/tree/master/plugins/python-build#building-with---enable-shared)
[How to reinstall already installed toolchains · Issue #34 · asdf-vm/asdf ](https://github.com/asdf-vm/asdf/issues/34)
[Getting Started  asdf ](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf)
[mac brew install python not in path](https://www.google.com/search?q=mac+brew+install+python+not+in+path&ie=UTF-8)
[homebrew - How do I use brew installed Python as the default Python?](https://stackoverflow.com/questions/5157678/how-do-i-use-brew-installed-python-as-the-default-python)
[Newsfeed — Nextdoor ](https://nextdoor.co.uk/p/cDFpyctGHm7Q?post=17592218312023&utm_source=email&is=npe&section=post&mar=true&ct=Q1D2_LKBGy353TlfXgxEn-2IiKfB3FMvUfIBddzBgTUYll0HtXuwPYXSIYizNBMN&ec=iD9EVf8Fqz_GipY9l9G7ig%3D%3D&mobile_deeplink_data=eyJhY3Rpb24iOiAidmlld19wb3N0IiwgInBvc3QiOiAxNzU5MjIxODMxMjAyM30%3D&link_source_user_id=17592189855531)

