import sys
input=sys.stdin.readline
n,m= map(int,input().split())
d={}
for _ in range(n):
    s=input().rstrip()
    if len(s)<m:continue
    else:d[s]=d.get(s,1)+1
l=sorted(d.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in l:print(i[0])