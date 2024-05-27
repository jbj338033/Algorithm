import sys
input=sys.stdin.readline
a=[0]
s=0
x=0
for _ in range(int(input())):
    i=input().split()
    n=int(i[0])
    if n==1:
        n=int(i[1])
        a.append(n)
        s+=n
        x^=n
    elif n==2:
        n=int(i[1])
        a.append(n)
        s-=n
        x^=n
    elif n==3:
        print(s)
    else:
        print(x)