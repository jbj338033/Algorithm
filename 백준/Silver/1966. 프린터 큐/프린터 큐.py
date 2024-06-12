from collections import deque
for _ in range(int(input())):
    n,m=map(int,input().split())
    q=deque(map(int,input().split()))
    r=deque(range(n))
    c=0
    while q:
        if q[0]==max(q):
            c+=1
            if r[0]==m:
                print(c)
                break
            q.popleft()
            r.popleft()
        else:
            q.append(q.popleft())
            r.append(r.popleft())

