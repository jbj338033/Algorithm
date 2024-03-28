import sys

queue = []

for _ in range(int(input())):
    s=sys.stdin.readline().split()
    c=s[0]

    if c == "push":queue.append(int(s[1]))
    elif c == "pop":print(queue.pop(0) if queue else -1)
    elif c == "size":print(len(queue))
    elif c == "empty":print(int(not bool(queue)))
    elif c == "front":print(queue[0] if queue else -1)
    else: print(queue[-1] if queue else -1)