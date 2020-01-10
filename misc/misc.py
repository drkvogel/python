"""
Learn python3 in Y Minutes (https://learnxinyminutes.com/docs/python3/)
"""

# given_name = input("What's your name? ")
print("Hello, {name}".format(name=given_name))

for i in range(3):
  print("an ting ", end="")
print("aye...")

for animal in ["cat", "dog", "rabbit"]:
  print("{} is a mammal".format(animal))

for i in range(10, 20, 2):
  print("i: {}".format(i), end=",")
print("i now: {}".format(i))

contents = {"aa": 12, "bb": 21}
with open("test.txt", "w+") as file:
    file.write(str(contents))

def varargs(*args):
  print(args)

varargs(1, 2, 3)

def keyword_args(**kwargs):
  print(kwargs)

keyword_args(big="foot", loch="ness")

def swap(x, y):
  return y, x

print(swap(1, 2)) # (2, 1)

def create_adder(x):
  def adder(y):
    return x + y
  return adder

add_10 = create_adder(10)
print("add_10(5): {}".format(add_10(5)))

print("list(map(add_10, [1,2,3])): {}".format(list(map(add_10, [1,2,3]))))

print(list(map(max, [1,2,3], [4,2,1])))

print(list(filter(lambda x: x > 5, [3,4,5,6,7])))
