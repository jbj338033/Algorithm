from collections import deque

n=int(input())
d=deque(range(1,n+1))

while len(d)>1:
    d.popleft()
    d.rotate(-1)
print(d[0])