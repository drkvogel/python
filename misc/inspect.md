
[How can I get the source code of a Python function?](https://stackoverflow.com/questions/427453/how-can-i-get-the-source-code-of-a-python-function)
[python - print the code which defined a lambda function](https://stackoverflow.com/questions/334851/print-the-code-which-defined-a-lambda-function)


```
>>> import inspect
>>> print("".join(inspect.getsourcelines(timed)[0]))
def timed(our_function):
  def our_wrapped_function(*args, **kwargs):
    start = time()
    result = our_function(*args, **kwargs)
    end = time()
    print(f'Time taken is {end-start} seconds.')
    return result
  return our_wrapped_function
```

