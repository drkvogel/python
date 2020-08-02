

[The Easy Guide to Python Command Line Arguments 😎 - Level Up Coding ](https://levelup.gitconnected.com/the-easy-guide-to-python-command-line-arguments-96b4607baea1)

see [argparse_1.py](argparse_1.py):

```
❯ python argparse_1.py --help
usage: argparse_1.py [-h]
A tutorial of argparse!
optional arguments:
  -h, --help  show this help message and exit

❯ python argparse_1.py --a 123
a: 123

❯ python argparse_1.py
a: 1

❯ python argparse_1.py --name
usage: argparse_1.py [-h] [--a A] [--name NAME]
argparse_1.py: error: argument --name: expected one argument

❯ python argparse_1.py --education university --a --b
usage: argparse_1.py [-h] [--name NAME] --education
                     {highschool,college,university,other} (--a | --b)
argparse_1.py: error: argument --b: not allowed with argument --a

```

[Argparse Tutorial — Python 3.8.3 documentation ](https://docs.python.org/3/howto/argparse.html)

```
❯ python argparse_1.py --education university --a source dest --name Chris
a: True
name: Chris
education: university
Has degree
source: "source"", dest: "dest"

❯ python argparse_1.py --help                                             
usage: argparse_1.py [-h] [--name NAME] --education
                     {highschool,college,university,other} [--c] [--d]
                     (--a | --b)
                     src dst

A tutorial of argparse!

positional arguments:
  src
  dst

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           Your name
  --education {highschool,college,university,other}
                        Your education level
  --c                   This is the 'c' variable
  --d                   This is the 'd' variable
  --a                   This is the 'a' variable
  --b                   This is the 'b' variable
  
```
