def f(n):
    if n%3==0 and n%5==0:return 'FizzBuzz'
    if n%3==0:return 'Fizz'
    if n%5==0:return 'Buzz'
    return str(n)

a,b,c=input(),input(),input()
if a[0]>='0' and a[0]<='9':print(f(int(a)+3));exit()
if b[0]>='0' and b[0]<='9':print(f(int(b)+2));exit()
if c[0]>='0' and c[0]<='9':print(f(int(c)+1))