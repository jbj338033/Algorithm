import sys
input=sys.stdin.readline
n=int(input())
l=[]
s=0
d=dict()
for _ in range(n):
    x=int(input())
    l.append(x)
    s+=x
    if x in d:d[x]+=1
    else:d[x]=1
l.sort()
print(round(s/n))
print(l[n//2])
m=max(d.values())
a=[]
for k,v in d.items():
    if v==m:a.append(k)
if len(a)==1:print(a[0])
else:print(sorted(a)[1])
print(l[-1]-l[0])