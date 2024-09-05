import sys
from collections import deque
input=sys.stdin.readline
q=deque()
for _ in range(int(input())):
    s=input().split()
    c=s[0]
    if c=='push_front':
        q.appendleft(int(s[1]))
    elif c=='push_back':
        q.append(int(s[1]))
    elif c=='pop_front':
        print(q.popleft() if q else -1)
    elif c=='pop_back':
        print(q.pop() if q else -1)
    elif c=='size':
        print(len(q))
    elif c=='empty':
        print(0 if q else 1)
    elif c=='front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)