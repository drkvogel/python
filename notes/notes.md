

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

four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

list

```py
for...in
if...in
len()
.append()
.insert()
.remove()
.pop()              # removes the specified index, (or the last item if index is not specified):
del thislist[0]     # delete list index
del thislist        # delete entire list
thislist.clear()    # empties the list
# construct list from tuple
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
append()	        # Adds an element at the end of the list
clear()	            # Removes all the elements from the list
copy()	            # Returns a copy of the list
count()	            # Returns the number of elements with the specified value
extend()	        # Add the elements of a list (or any iterable), to the end of the current list
index()	            # Returns the index of the first element with the specified value
insert()	        # Adds an element at the specified position
pop()	            # Removes the element at the specified position
remove()	        # Removes the item with the specified value
reverse()	        # Reverses the order of the list
sort()	            # Sorts the list
```

tuples

a tuple is a collection which is ordered and unchangeable

```py
thistuple = tuple(("apple", "banana", "cherry"))
for...in
if...in
len()
del thistuple
count()	            # Returns the number of times a specified value occurs in a tuple
index()	            # Searches the tuple for a specified value and returns the position of where it was found
```

sets

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
intersection_update()   	                        # Removes the items in this set that are not present in other, specified set(s)
isdisjoint()    	                        # Returns whether two sets have a intersection or not
issubset()  	                        # Returns whether another set contains this set or not
issuperset()    	                        # Returns whether this set contains another set or not
pop()   	                        # Removes an element from the set
remove()    	                        # Removes the specified element
symmetric_difference()  	                        # Returns a set with the symmetric differences of two sets
symmetric_difference_update()   	                        # inserts the symmetric differences from this set and another
union() 	                        # Return a set containing the union of sets
update()    	                        # Update the set with the union of this set and others
```

How strict is python about double quotes vs single quotes in parameters? : learnpython (https://www.reddit.com/r/learnpython/comments/8030b7/how_strict_is_python_about_double_quotes_vs/)
>single vs double quotes: "PEP 8 says pick one and use it consistently."

