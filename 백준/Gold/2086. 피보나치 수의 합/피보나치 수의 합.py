import sys
d={1:1,2:1}
def f(n):
  if d.get(n):
    return d[n]
  else:
    if n%2 == 1:
      d[n]=(f(n//2)**2+f(n//2+1)**2)%1000000000
    else:
      d[n]=(f(n+1)-f(n-1))%1000000000
    return d[n]
a,b=map(int,sys.stdin.readline().split())
print((f(b+2)-f(a+1))%1000000000)