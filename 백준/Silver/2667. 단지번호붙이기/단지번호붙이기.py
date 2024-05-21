def dfs(x,y):
    global c
    visited[x][y] = True
    c+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:continue
        if graph[nx][ny]==1 and not visited[nx][ny]:dfs(nx, ny)
n=int(input())
graph=[]
visited=[[False]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
r=[]
for _ in range(n):graph.append(list(map(int, input())))
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            c=0
            dfs(i, j)
            r.append(c)
r.sort()
print(len(r))
for r in r:print(r)