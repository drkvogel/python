
py.test - old version of pytest? yes
[python - "py.test" vs "pytest" command](https://stackoverflow.com/questions/39495429/py-test-vs-pytest-command)
>The `py.test` invocation *is the old and busted joint*. `pytest` *is the new hotness* (since 3.0). py.test and pytest invocations will coexist for a long time I guess, but at some point py.test might be deprecated. So I would recommend to #dropthedot.

[Nose alternatives - nose2, pytest or something else? : Python ](https://www.reddit.com/r/Python/comments/3ys29v/nose_alternatives_nose2_pytest_or_something_else/)

>nerdwaller 4 years ago I switched to py.test and love it. The debugging is great (prints context of the failure), fixtures, parametrization, markers, and parallel/distributed running are the reasons that come quickly to mind.

Edit: expanding on the reasons:
* It uses the built in, simple, assert check, no need to know self.assertEquals and all the variants, just plug in some boolean value.
```py
assert 1 == 1, 'This is my error message, which is optional'
```

* Fixtures: These aren't the setup/teardown fixtures (per-se), but more like dependency injection (and are incredibly useful). You can even inject a fixture into a fixture (say you need to log in a user, but you need an HTTP client for it to work, you probably use that client elsewhere so DRY it up):
```py
@pytest.fixture 
def logged_in_user(): 
    # complicated user login logic return my_user

def test_user_can_access_resource(logged_in_user): 
    # Do stuff with the logged in user!
```

* Markers: Easy way to categorize tests (and coincidentally run only those groups)
```py
@pytest.mark.slow 
def test_slow_running_thing(): 
    time.sleep(500) # Woah, you probably don't want to run that for every check in...
```

* Parallel execution via a plugin, `xdist`. I saw insane speed improvements, figure that! The reporter can collect all independent tests in one report (say you use jenkins and need a junit style xml).

* Parametrization. This is just saying "rerun this same test, each as a unique test report, with different inputs", it's awesome because my testing philosophy is usually "Zero, One, and Many" (expanding to include edge cases as they come up). Want a quick 7 tests written (see the output below for how that is done):

[PyTest Tutorial: What is, Install, Fixture, Assertions ](https://www.guru99.com/pytest-tutorial.html)

[The Cleaning Hand of Pytest - Daftcode Blog ](https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684)
>For many developers the choice of their test framework might be simple — Pytest.

