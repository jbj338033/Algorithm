import heapq, sys
n=int(input())
h=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        print(heapq.heappop(h)[1] if h else 0)
    else:
        heapq.heappush(h,(abs(x),x))
