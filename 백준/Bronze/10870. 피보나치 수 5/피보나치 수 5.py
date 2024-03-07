fib = lambda n, a=0, b=1 : a if n<=0 else fib(n-1,b, a+b)

print(fib(int(input())))