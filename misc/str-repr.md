
[python - What is the difference between __str__ and __repr__?](https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr)
>Unless you specifically act to ensure otherwise, most classes don't have helpful results for either - no difference, and no info beyond the class and object's id
> if you override __repr__, that's ALSO used for __str__, but not vice versa.
>__repr__ goal is to be unambiguous
>__str__ goal is to be readable
>Container’s __str__ uses contained objects’ __repr__

>__repr__: representation of python object usually eval will convert it back to that object
>__str__: is whatever you think is that object in text form

>hardly anybody bothers making the __repr__ of objects be a string that eval may use to build an equal object (it's just too hard, AND not knowing how the relevant module was actually imported makes it actually flat out impossible). So, my advice: focus on making __str__ reasonably human-readable, and __repr__ as unambiguous as you possibly can, even if that interferes with the fuzzy unattainable goal of making __repr__'s returned value acceptable as input to __eval__!

