
[Prerequisites and Assumptions ](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html)

[Releases · mozilla/geckodriver ](https://github.com/mozilla/geckodriver/releases)
```
20/05/29 2:57:26 kvogel-macbook-2018:~/Downloads
❯ tar xzf geckodriver-v0.26.0-macos.tar.gz
❯ which chromedriver
/usr/local/bin/chromedriver
❯ mv geckodriver /usr/local/bin
❯ which geckodriver
/usr/local/anaconda3/bin/geckodriver
❯ which -a geckodriver
/usr/local/anaconda3/bin/geckodriver
/usr/local/bin/geckodriver
```




```
20/05/29 2:01:31 kvogel-macbook-2018:~/Projects/python/misc ±(master) ✗ 
❯ pip list | grep django
django-heroku                      0.3.1              
djangorestframework                3.11.0    
```

```
(base) 20/05/28 15:17:07 kvogel-macbook-2018:~/Downloads/tmp
❯ conda activate conda-env
(conda-env) 20/05/28 15:17:11 kvogel-macbook-2018:~/Downloads/tmp
❯ python
Python 3.7.3 | packaged by conda-forge | (default, Jul  1 2019, 14:38:56)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
>>> import django
>>> print (django.get_version())
3.0.5
```

```
20/05/28 23:20:38 kvogel-macbook-2018:~/po
❯ python
Python 3.7.3 | packaged by conda-forge | (default, Jul  1 2019, 14:38:56)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'3.0.5'
```

?

```
20/05/29 2:01:49 kvogel-macbook-2018:~/Projects/python/misc ±(master) ✗ 
❯ cd ../tdd/testinggoat 
20/05/29 2:59:47 kvogel-macbook-2018:~/Projects/python/tdd/testinggoat ±(master) ✗ 
❯ deactivate 
DeprecationWarning: 'source deactivate' is deprecated. Use 'conda deactivate'.
❯ pip list | grep django
django-heroku                      0.3.1              
djangorestframework                3.11.0             
❯ python3.6 -m venv venv
❯ . ./venv/bin/activate
(venv) 20/05/29 3:00:57 kvogel-macbook-2018:~/Projects/python/tdd/testinggoat ±(master) ✗ 
❯ pip install "django<1.12" "selenium<4"
```
