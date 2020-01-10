
[Python Tuples ](https://www.w3schools.com/python/python_tuples.asp)


>To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
```py
>>> thistuple = ("apple")
>>> type(thistuple)
<class 'str'>
>>> thistuple = ("apple",)
>>> type(thistuple)   
<class 'tuple'>
```

>Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called. But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
```py
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
```
