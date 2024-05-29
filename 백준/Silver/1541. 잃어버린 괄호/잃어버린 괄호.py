s=input().split('-')
l=[]
for i in s:
    s=0
    t=i.split('+')
    for j in t:s+=int(j)
    l.append(s)
n=l[0]
for i in l[1:]:
    n-=i
print(n) 