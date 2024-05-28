import sys
from collections import deque
input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
c=1
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
q=deque([r])
visited[r]=1
while q:
    v=q.popleft()
    graph[v].sort(reverse=1)
    for i in graph[v]:
        if not visited[i]:
            c+=1
            visited[i]=c
            q.append(i)
for i in visited[1:]:
    print(i)