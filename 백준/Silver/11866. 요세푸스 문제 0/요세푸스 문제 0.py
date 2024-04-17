from collections import deque

n,k=map(int,input().split())

l=deque(range(1,n+1))
s=[]

while l:
    l.rotate(-k+1)
    s.append(str(l.popleft()))
print('<',', '.join(s),'>',sep='')