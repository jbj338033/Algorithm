def factorial(n):
    r = 1

    if n > 0:
        r = n * factorial(n - 1)
    return r

print(factorial(int(input())))