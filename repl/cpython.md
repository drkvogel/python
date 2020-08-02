


history with arrow keys escape sequences

```
20/03/17 19:32:32 kvogel-macbook-2018:~/pw/sherpa-brain-py2 ±(master) ✗
❯ conda install readline
Collecting package metadata (current_repodata.json): done
Solving environment: done
## Package Plan ##
  environment location: /usr/local/anaconda3
  added / updated specs:
    - readline
The following packages will be downloaded:
    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2019.11.28 |       hecc5488_0         145 KB  conda-forge
    certifi-2019.11.28         |   py37hc8dfbb8_1         148 KB  conda-forge
    conda-4.8.3                |   py37hc8dfbb8_1         3.0 MB  conda-forge
    python_abi-3.7             |          1_cp37m           4 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         3.3 MB
The following NEW packages will be INSTALLED:
  python_abi         conda-forge/osx-64::python_abi-3.7-1_cp37m
The following packages will be UPDATED:
  ca-certificates                      2019.9.11-hecc5488_0 --> 2019.11.28-hecc5488_0
  certifi                                  2019.9.11-py37_0 --> 2019.11.28-py37hc8dfbb8_1
  conda                                       4.7.12-py37_0 --> 4.8.3-py37hc8dfbb8_1
Proceed ([y]/n)? y
```
no dice


```
20/03/18 10:26:44 kvogel-macbook-2018:~/pw/sherpa-brain-py2 ±(master) ✗
❯ python
Python 3.7.3 | packaged by conda-forge | (default, Jul  1 2019, 14:38:56)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import readline
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: dlopen(/usr/local/anaconda3/lib/python3.7/lib-dynload/readline.cpython-37m-darwin.so, 2): Library not loaded: @rpath/libncurses.6.dylib
  Referenced from: /usr/local/anaconda3/lib/libreadline.8.dylib
  Reason: image not found
>>> import gnureadline
>>>
```