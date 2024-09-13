import sys
a=[0]*10
e=int(sys.stdin.readline())
p=1
s=1
def f(x,p):
    while x>0:
        a[x%10]+=p
        x//=10
while s<=e:
    while e%10!=9:
        f(e,p)
        e-=1
    if e < s:break
    while s%10!=0:
        f(s,p)
        s+=1
    s//=10
    e//=10
    for i in range(10):a[i]+=(e-s+1)*p
    p*=10
print(*a)