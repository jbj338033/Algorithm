n,k=int(input()),int(input())
s,e=1,k
while s<=e:
    m=(s+e)//2
    t=0
    for i in range(1,n+1):
        t+=min(m//i,n)
    if t>=k:
        a=m
        e=m-1
    else:s=m+1
print(a)