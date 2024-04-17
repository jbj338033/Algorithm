def dfs(v):
    global c
    visited[v] = True
    # print(v,end=' ')
    c+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n=int(input())

graph=[[] for _ in range(n+1)]
visited=[False] * (n+1)
c=0

for _ in range(int(input())):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(1)
print(c-1)