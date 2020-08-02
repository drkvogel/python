import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
# parser.add_argument("--a")
# parser.add_argument("--a", default=1, help="This is the 'a' variable")
parser.add_argument("--name", default=None, type=str, help="Your name")
parser.add_argument("--education", 
                    choices=["highschool", "college", "university", "other"],
                    required=True, type=str, help="Your education level")

parser.add_argument("--c", action="store_true", help="This is the 'c' variable")
  # given `--c`: c=True, else c=False
parser.add_argument("--d", action="store_const", const=10, help="This is the 'd' variable")
  # given `--d`: d=10, else d=None

# mutually exclusive group "store_true":
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--a", action="store_true", help="This is the 'a' variable")
group.add_argument("--b", action="store_true", help="This is the 'b' variable")
  # no `--a` or `--b`: argparse_1.py: error: one of the arguments --a --b is required
  # both `--a --b`: argparse_1.py: error: argument --b: not allowed with argument --a

# positional arguments
parser.add_argument("src")
parser.add_argument("dst")

args = parser.parse_args()
a = args.a
name = args.name
ed = args.education
print(f'a: {a}')
print(f'name: {name}')
print(f'education: {ed}')

if ed == "college" or ed == "university":
    print("Has degree")
elif ed == "highschool":
  print("Finished Highschool")
else:
    print("Does not have degree")

print(f'source: "{args.src}"", dest: "{args.dst}"')
# print(f'args: {args}')


