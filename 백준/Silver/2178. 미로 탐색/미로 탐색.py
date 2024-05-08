from collections import deque
def bfs(v):
    q=deque()
    q.append(v)
    visited[v[0]][v[1]]=True
    while q:
        x,y,c=q.popleft()
        if x==n-1 and y==m-1:return c
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and l[nx][ny]==1 and not visited[nx][ny]:
                q.append((nx,ny,c+1))
                visited[nx][ny]=True
    return -1
n,m=map(int,input().split())
l=[list(map(int,input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
v=(0,0,1)
print(bfs(v))