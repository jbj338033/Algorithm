import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
n,k=map(int,input().split())
print((f(n) // (f(n-k) * f(k)))%10007)