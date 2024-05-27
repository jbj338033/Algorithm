from collections import deque
n,m=map(int,input().split())
l=[]
q=deque([])
visited=[[0] * m for _ in range(n)]
r=[[-1]*m for _ in range(n)]
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        if a[j]==2:
            q.append((i,j))
            visited[i][j]=True
            r[i][j]=0
        if a[j]==0:
            r[i][j]=0
    l.append(a)
d=[(1,0),(-1,0),(0,1),(0,-1)]
while q:
    y,x=q.popleft()
    for dx,dy in d:
        ny,nx=y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and l[ny][nx]==1:
            q.append((ny,nx))
            visited[ny][nx]=True
            r[ny][nx]=r[y][x]+1
for i in r:
    print(*i)