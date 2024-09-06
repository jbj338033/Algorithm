import sys
from collections import deque
input=sys.stdin.readline
s=input().rstrip()
l,r=deque(s),deque()
for _ in range(int(input())):
    a=input().split()
    c=a[0]
    if c=='L':
        if l:r.appendleft(l.pop())
    elif c=='D':
        if r:l.append(r.popleft())
    elif c=='B':
        if l:l.pop()
    else:
        l.append(a[1])
print(*(l+r),sep='')