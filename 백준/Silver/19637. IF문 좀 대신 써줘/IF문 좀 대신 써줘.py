import sys
input=sys.stdin.readline
n,m=map(int,input().split())
p=[]
for _ in range(n):
    s=input().split()
    p.append((s[0],int(s[1])))
for _ in range(m):
    x=int(input())
    l,r=0,n-1
    while l<r:
        m=(l+r)//2
        if p[m][1]>=x:
            r=m
        else:
            l=m+1
    print(p[l][0])