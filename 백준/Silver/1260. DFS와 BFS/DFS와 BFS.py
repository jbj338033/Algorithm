from collections import deque

def dfs(v):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
def bfs(v):
    q=deque([v])
    visited[v]=True
    while q:
        v=q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited=[False]*(n+1)
dfs(v)
print()
visited=[False]*(n+1)
bfs(v)