
def fib(n):
    a, b = 0, 1
    while b < n:
        # print(b)
        yield a
        a, b = b, a + b

# >>> print([i for i in fib(30)])
# [0, 1, 1, 2, 3, 5, 8, 13]

# [python - What does the "yield" keyword do?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
