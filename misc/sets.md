
### sets

```py
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
print("banana" in thisset)
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
print(len(thisset))
thisset.remove("banana")    # If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana")   # If the item to remove does not exist, discard() will NOT raise an error.
thisset.clear()
del thisset
thisset = set(("apple", "banana", "cherry"))
add()   	                        # Adds an element to the set
clear() 	                        # Removes all the elements from the set
copy()  	                        # Returns a copy of the set
difference()    	                # Returns a set containing the difference between two or more sets
difference_update() 	            # Removes the items in this set that are also included in another, specified set
discard()   	                    # Remove the specified item
intersection()  	                # Returns a set, that is the intersection of two other sets
intersection_update()   	        # Removes the items in this set that are not present in other, specified set(s)
isdisjoint()    	                # Returns whether two sets have a intersection or not
issubset()  	                    # Returns whether another set contains this set or not
issuperset()    	                # Returns whether this set contains another set or not
pop()   	                        # Removes an element from the set
remove()    	                    # Removes the specified element
symmetric_difference()  	        # Returns a set with the symmetric differences of two sets
symmetric_difference_update()   	# inserts the symmetric differences from this set and another
union() 	                        # Return a set containing the union of sets
update()    	                    # Update the set with the union of this set and others
```

[Sets - Learn Python - Free Interactive Python Tutorial ](https://www.learnpython.org/en/Sets)

`set()` inbuilt function
`{}` notation

cannot contain duplicates:
```py
>>> e = {1, 1, 2, 3}
>>> e
{1, 2, 3}
```

```py
>>> myset = set("My name is Chris and Chris is my name")
>>> myset
{'y', 'n', 'e', 'm', 'a', 'r', 'h', 's', 'C', 'i', 'd', 'M', ' '}

>>> myset = set("my name is Chris and Chris is my name".split())
>>> myset
{'Chris', 'and', 'my', 'name', 'is'}

>>> a = set(["Jake", "John", "Eric"])
>>> b = set(["John", "Jill"])
>>> a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'

unsupported operand type(s) for +: 'set' and 'set'
>>> a.union(b)
{'John', 'Jill', 'Eric', 'Jake'}

>>> a.intersection(b)
{'John'}

>>> a.difference(b)
{'Eric', 'Jake'}

>>> b.difference(a)
{'Jill'}

>>> b.symmetric_difference(a)
{'Jill', 'Jake', 'Eric'}

>>> a.symmetric_difference(b)
{'Eric', 'Jill', 'Jake'}

>>>
```

`{}` notation:
```py
>>> c = {1, 2, 3}
>>> c
{1, 2, 3}

>>> type(c)
<class 'set'>

>>> d = {3, 4, 5}
>>> c.union(d)
{1, 2, 3, 4, 5}
>>> c.symmetric_difference(d)
{1, 2, 4, 5}
>>> c.intersection(d)
{3}
```
