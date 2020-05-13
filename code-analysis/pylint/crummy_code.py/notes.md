

```
20/02/9 14:58:10 kvogel-macbook-2018:~/Projects/python/code-analysis/pylint/crummy_code.py ±(master) ✗ 
❯ pylint crummy_code_fixed.py
************* Module crummy_code_fixed
crummy_code_fixed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
crummy_code_fixed.py:3:0: W0105: String statement has no effect (pointless-string-statement)
crummy_code_fixed.py:5:0: C0112: Empty class docstring (empty-docstring)
crummy_code_fixed.py:15:24: E0602: Undefined variable 'platform' (undefined-variable)
crummy_code_fixed.py:18:22: E1121: Too many positional arguments for method call (too-many-function-args)
crummy_code_fixed.py:20:4: C0103: Method name "getWeight" doesn't conform to snake_case naming style (invalid-name)
crummy_code_fixed.py:20:4: C0112: Empty method docstring (empty-docstring)
crummy_code_fixed.py:20:4: E0213: Method should have "self" as first argument (no-self-argument)
crummy_code_fixed.py:20:4: R0201: Method could be a function (no-self-use)
crummy_code_fixed.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)
crummy_code_fixed.py:1:0: W0611: Unused import sys (unused-import)
```

[R0201: Method could be a function (no-self-use)](https://www.google.com/search?q=R0201%3A+Method+could+be+a+function+(no-self-use)&ie=UTF-8)
[python - How to handle the pylint message: Warning: Method could be a function](https://stackoverflow.com/questions/2674035/how-to-handle-the-pylint-message-warning-method-could-be-a-function)
[Method could be a function — Python Anti-Patterns documentation ](https://docs.quantifiedcode.com/python-anti-patterns/correctness/method_could_be_a_function.html)
