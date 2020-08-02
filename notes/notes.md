

[python execute a .py file from another](https://www.google.com/search?q=python+execute+a+.py+file+from+another&ie=UTF-8)
[How can I make one python file run another?](https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another)
[python - What is the best way to call a script from another script?](https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script)
    
[scripting - Get name of current script in Python](https://stackoverflow.com/questions/4152963/get-name-of-current-script-in-python)
>Use `__file__`. If you want to omit the directory part (which might be present), you can use `os.path.basename(__file__)`.

[How to Convert Python Class Object to JSON? – 2 Python Examples ](https://pythonexamples.org/convert-python-class-object-to-json/)
```py
# convert to JSON string
jsonStr = json.dumps(my_instance.__dict__)
```

[python if defined](https://www.google.com/search?q=python+if+defined&ie=UTF-8)
[Testing if a variable is defined « Python recipes « ActiveState Code ](http://code.activestate.com/recipes/59892-testing-if-a-variable-is-defined/)
[Determine if variable is defined in Python](https://stackoverflow.com/questions/1592565/determine-if-variable-is-defined-in-python)
[python - Pythonic way to check if something exists?](https://stackoverflow.com/questions/9390126/pythonic-way-to-check-if-something-exists)



[types - How can I check if my python object is a number?](https://stackoverflow.com/questions/4187185/how-can-i-check-if-my-python-object-is-a-number)
```py
if isinstance(x, numbers.Number):
  # ok
# bools are numbers. To exclude:
if isinstance(x, (int, float, complex)) and not isinstance(x, bool):
  # ok
```
but this is not EAFP so not pythonic!

### EAFP (Easier to ask for forgiveness than permission)

[What is the EAFP principle in Python?](https://stackoverflow.com/questions/11360858/what-is-the-eafp-principle-in-python)
>Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.
>*Prefer EAFP* when coding in Python, because it is *generally more reliable*.

EAFP (Easier to ask for forgiveness than permission):
```py
try:
    x = my_dict["key"]
except KeyError:
    # handle missing key
```
LBYL (look before you leap):
```py
if "key" in my_dict:
    x = my_dict["key"]
else:
    # handle missing key
```

[notes/wsgi.md](/notes/wsgi.md)

### Swagger / OpenAPI (OAS)

Today, the most commonly used definition for APIs is the OpenAPI Specification. The OpenAPI Specification (OAS), which is based on the original Swagger Specification, defines RESTful standards for APIs. OAS Definitions map resources and operations for an API.

Docstrings

three numeric types in Python: int float complex
type() function: print(type(x))

Casting is done using constructor functions: int() float() str()

a.strip()
a.split()
len()

input()

### collection data types

four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

[misc/lists.md](/misc/lists.md)
[misc/tuples.md](/misc/tuples.md)
[misc/sets.md](/misc/sets.md)

[How strict is python about double quotes vs single quotes in parameters? : learnpython ](https://www.reddit.com/r/learnpython/comments/8030b7/how_strict_is_python_about_double_quotes_vs/)
>single vs double quotes: "PEP 8 says pick one and use it consistently."


bpython - better python REPL: `pip3 install bpython`


[Nine simple steps for better-looking python code - Towards Data Science ](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)
[Python 3, you can add type annotations](https://www.google.com/search?q=Python+3%2C+you+can+add+type+annotations&ie=UTF-8)
[Welcome to Mypy documentation! — Mypy 0.770 documentation ](https://mypy.readthedocs.io/en/stable/)
[pre-commit ](https://pre-commit.com/#plugins)
[DeepSource: Find and fix issues during code reviews ](https://deepsource.io/)
[DeepCode  From Code to Predictions ](https://www.deepcode.ai/)
[Sourcegraph documentation - Sourcegraph docs ](https://docs.sourcegraph.com/#quickstart-guide)
[psf/black: The uncompromising Python code formatter ](https://github.com/psf/black)
[Consistent Python code with Black · Matt Layman ](https://www.mattlayman.com/blog/2018/python-code-black/)
[pre-commit ](https://pre-commit.com/)
[Flake8: Your Tool For Style Guide Enforcement — flake8 3.7.9 documentation ](https://flake8.pycqa.org/en/latest/)
[Flake8: Your Tool For Style Guide Enforcement — flake8 3.7.9 documentation ](https://flake8.pycqa.org/en/latest/)
[Quantum Monte Carlo of the Hubbard model](https://www.google.com/search?q=Quantum+Monte+Carlo+of+the+Hubbard+model&ie=UTF-8)
[Hubbard model - Wikipedia ](https://en.wikipedia.org/wiki/Hubbard_model)
[Quantum Monte Carlo](https://www.google.com/search?q=Quantum+Monte+Carlo&ie=UTF-8)
[Quantum Monte Carlo - Wikipedia ](https://en.wikipedia.org/wiki/Quantum_Monte_Carlo)


some podcast I was listening to:
native testing
why is python slow?
kyle let go from his job due to pandemic
christopher bailey
[About Anthony Shaw – Real Python ](https://realpython.com/team/ashaw/)
why can't I be doing cool stuff like this instsead of nightmare scenarios?
