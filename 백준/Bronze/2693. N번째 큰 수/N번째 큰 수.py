import heapq
for _ in range(int(input())):
    print(sorted(map(int,input().split()), reverse=True)[2])