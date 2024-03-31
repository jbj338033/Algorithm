from sys import stdin
from collections import deque

d=deque()

for _ in range(int(input())):
    s=stdin.readline().split()
    c=s[0]

    if c == "push_front":
        d.appendleft(s[1])
    elif c == "push_back":
        d.append(s[1])
    elif c == "pop_front":
        print(d.popleft() if d else -1)
    elif c == "pop_back":
        print(d.pop() if d else -1)
    elif c == "size":
        print(len(d))
    elif c == "empty":
        print(int(not bool(d)))
    elif c == "front":
        print(d[0] if d else -1)
    elif c == "back":
        print(d[-1] if d else -1)