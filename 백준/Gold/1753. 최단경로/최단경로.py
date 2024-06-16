import sys
import heapq
input=sys.stdin.readline
inf=1e9
v,e=map(int, input().split())
k=int(input())
graph=[[] for _ in range(v+1)]
d=[inf]*(v+1)
for _ in range(e):
    u,V,w=map(int, input().split())
    graph[u].append((V,w))
q=[]
heapq.heappush(q,(0,k))
d[k]=0
while q:
    a,b=heapq.heappop(q)
    if d[b]<a:continue
    for i in graph[b]:
        c=a+i[1]
        if c<d[i[0]]:
            d[i[0]]=c
            heapq.heappush(q,(c,i[0]))
for i in range(1,v+1):print("INF" if d[i]==inf else d[i])