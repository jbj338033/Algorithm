import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:i.sort()
c=0
visited=[0]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        c+=1
print(c)