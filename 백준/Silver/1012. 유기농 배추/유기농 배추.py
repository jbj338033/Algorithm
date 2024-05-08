import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:return
    if graph[x][y]==1 and not visited[x][y]:
        visited[x][y]=True
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
for _ in range(int(input())):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    visited=[[False]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and not visited[i][j]:
                dfs(i,j)
                count+=1
    print(count)