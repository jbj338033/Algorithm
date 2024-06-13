n,k=map(int,input().split())
v=[0]*100001
q=[n]
while q:
    x=q.pop(0)
    if x==k:print(v[x]);break
    for nx in (x-1,x+1,x*2):
        if 0<=nx<100001 and not v[nx]:
            v[nx]=v[x]+1
            q.append(nx)