n,m=map(int,input().split())
s=set()
c=0
for _ in range(n):
    s.add(input())
for _ in range(m):
    if input() in s:c+=1
print(c)