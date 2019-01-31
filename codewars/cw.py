#!/usr/bin/env python

def accum(s):
    words = []
    for i, x in enumerate(s, 1):
        words.append((x.lower()*i).capitalize())
    return '-'.join(words)

print(accum('abcd'))

# def friend(x):
#     friends = []
#     for i in x:
#         if len(i) == 4:
#             friends.append(i)
#     return friends

def friend(x):
    return list(filter(lambda p: len(p) == 4, x))
    # In py2, filter returns a list. In py3, filter returns an iterable filter object, 
    # which has to be transformed into a list for the purposes of this kata.

# print(friend(["Ryan", "Kieran", "Mark",]))

# def smallestInt(arr):
#     return min(arr)