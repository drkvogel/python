
# Demystifying Python Decorators | Level Up Coding (https://levelup.gitconnected.com/demystifying-python-decorators-726f04963a52)

from time import time

def timed(our_function):
    def our_wrapped_function(*args, **kwargs):
        start = time()
        result = our_function(*args, **kwargs)
        end = time()
        print(f'Time taken is {end-start} seconds.')
        return result
    return our_wrapped_function

@timed
def decorated_func():
    print('this is decorated_func() decorated with @timed')
    import traceback, inspect
    print(f'func name from stack: {traceback.extract_stack(None, 2)[0][2]}.')
    # How to get a function name as a string? - Stack Overflow (https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string)
    stack = traceback.extract_stack()
    print(stack[len(stack)-1][2])
    print(inspect.getouterframes(inspect.currentframe())[1][1:4][2])



'''
❯ cd ~/p/python/misc
20/03/16 0:23:15 kvogel-macbook-2018:~/p/python/misc ±(master) ✗
❯ ptpython
>>> import decorators
>>> decorators.timed
<function timed at 0x10b18ff28>
>>> from decorators import *
>>> def func():
...     print('func')
>>> timed_func = timed(func)
>>> timed_func()
func
Time taken is 1.4781951904296875e-05 seconds.
>>>
'''

'''
>>> import decorators
>>> from decorators import *
>>> decorated_func()
this is decorated_func() decorated with @timed
func name from stack: our_wrapped_function.
Time taken is 0.000209808349609375 seconds.
'''
