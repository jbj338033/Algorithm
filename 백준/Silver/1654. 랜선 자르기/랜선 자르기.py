k,n=map(int,input().split())
l=[int(input()) for _ in range(k)]
s=1
e=max(l)
while s<=e:
    m=(s+e)//2
    t=0
    for i in l:t+=i//m
    if t>=n:
        s=m+1
    else:
        e=m-1
print(e)