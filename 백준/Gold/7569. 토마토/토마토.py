m,n,h=map(int,input().split())
l=[[[*map(int,input().split())] for _ in range(n)]for _ in range(h)]
d=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
q=[]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if l[i][j][k]==1:q.append((i,j,k))
c=0
while q:
    t=[]
    for i,j,k in q:
        for x,y,z in d:
            if 0<=i+x<h and 0<=j+y<n and 0<=k+z<m and l[i+x][j+y][k+z]==0:
                l[i+x][j+y][k+z]=1
                t.append((i+x,j+y,k+z))
    q=t
    if q:c+=1
for i in l:
    for j in i:
        if 0 in j:
            c=-1
            break
    if c==-1:break
print(c)
