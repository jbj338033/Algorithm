from collections import deque

n,m=map(int,input().split())
d=deque(range(1,n+1))
cnt=0
for a in map(int,input().split()):
    i=d.index(a)

    if i == 0:
        d.popleft()
        continue

    r=len(d)-i

    if i <= r:
        d.rotate(-i)
        cnt+=i
    else:
        d.rotate(r)
        cnt+=r
    d.popleft()
print(cnt)