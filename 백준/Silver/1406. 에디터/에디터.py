from collections import deque
import sys

s=input()
l=deque(s)
r=deque()

for _ in range(int(input())):
    a=sys.stdin.readline().split()
    c=a[0]

    if c == 'L' and l:r.appendleft(l.pop())
    elif c == 'D' and r:l.append(r.popleft())
    elif c == 'B' and l:l.pop()
    elif c == 'P':
        v=a[1]
        l.append(v)
print(*l,*r,sep='')

