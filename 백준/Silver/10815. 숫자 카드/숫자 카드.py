n=int(input())
nl=list(map(int,input().split()))
m=int(input())
ml=list(map(int,input().split()))
d={}
for i in ml:
    d[i]=0
for i in nl:
    if i in d:
        d[i]=1
for i in d:
    print(d[i],end=' ')