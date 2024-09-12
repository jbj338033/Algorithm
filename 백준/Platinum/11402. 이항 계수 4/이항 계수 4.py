def l(n,k): 
    if n<k:return 0
    elif n==k:return 1 
    x=1
    for i in range(1,k+1):
        x*=n-i+1
        x//=i
    return x
import sys
n,k,m=map(int,sys.stdin.readline().split())
a,b=[],[]
cnt=0
while n or k:
    a.append(n%m)
    b.append(k%m)
    n//=m
    k//=m
r=1
for i in range(len(a)):
    r*=l(a[i],b[i]) 
    r%=m
print(r)