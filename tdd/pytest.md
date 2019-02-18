


Updated `pytest` with `pip install -U pytest` to 4.2.0, but on running, got [AttributeError: 'Function' object has no attribute 'get_marker'](https://github.com/pytest-dev/pytest-cov/issues/252). tried `conda install pytest-cov pytest-remotedata` via [Fix pytest AttributeError Function object has no attribute get_marker](https://www.scivision.co/pytest-attribute-error-getmarker/), no dice.
Downgraded to latest 3.x.x with `pip install pytest==3.10.1` via [Changelog history](https://docs.pytest.org/en/latest/changelog.html), works...

test funcs have to begin with `test` (no trailing underscore necessary), but files don't