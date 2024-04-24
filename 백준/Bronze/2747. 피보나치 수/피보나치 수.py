import sys
sys.setrecursionlimit(100000)

def f(n):
    a,b=1,1
    if n==1 or n==2:
        return 1
    for _ in range(1,n):
        a,b=b,a+b
    return a
n=int(input())
l=[f(i) for i in range(1,n+1)]
print(l[n-1])