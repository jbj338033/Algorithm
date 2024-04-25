import heapq, sys
n=int(input())
h=[]
for _ in range(n):
    for i in map(int, sys.stdin.readline().split()):
        heapq.heappush(h, i)
        if len(h)>n:
            heapq.heappop(h)
h2=[]
for i in h:
    heapq.heappush(h2, (-i,i))
for _ in range(n-1):
    heapq.heappop(h2)
print(heapq.heappop(h2)[1])