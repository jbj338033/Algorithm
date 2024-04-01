from collections import deque
import sys

d=deque()

for _ in range(int(input())):
    s=sys.stdin.readline().split()
    c=int(s[0])
    
    if c == 1:
        d.appendleft(s[1])
    elif c == 2:
        d.append(s[1])
    elif c == 3:
        print(d.popleft() if d else -1)
    elif c == 4:
        print(d.pop() if d else -1)
    elif c == 5:
        print(len(d))
    elif c == 6:
        print(int(not bool(d)))
    elif c == 7:
        print(d[0] if d else -1)
    else:
        print(d[-1] if d else -1)