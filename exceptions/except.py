
def something():
  # raise -1
  # raise ValueError
  raise ValueError('This is my error')
  # raise "my error" # don't


try:
    something()
except ValueError as error:
    print('An exception occurred: {}'.format(error)) # 'This is my error'
except BaseException as error: # catches everything? even -1
    print('An exception occurred: {}'.format(error))
      # exceptions must derive from BaseException
    print('type: ' + type(error).__name__) # returns the name of the exception


'''
https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
Only valid in much older versions of Python (2.4 and lower), you may still see people raising strings:

raise 'message' # really really wrong. don't do this.

In Python3 there are 4 different syntaxes for rasing exceptions:

1. raise exception 
2. raise exception (args) 
3. raise
4. raise exception (args) from original_exception
'''
