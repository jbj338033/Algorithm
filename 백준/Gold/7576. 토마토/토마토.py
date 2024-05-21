from collections import deque
def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and t[nx][ny]==0:
                t[nx][ny]=t[x][y]+1
                q.append((nx,ny))
m,n=map(int,input().split())
t=[list(map(int,input().split())) for _ in range(n)]
q=deque()
dx,dy=[-1,1,0,0],[0,0,-1,1]
for i in range(n):
    for j in range(m):
        if t[i][j]==1:q.append((i,j))
bfs()
r=0
for i in t:
    if 0 in i:
        r=-1
        break
    r=max(r, max(i))
print(r if r==-1 else r-1)