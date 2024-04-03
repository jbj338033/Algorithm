a,b=map(int,input().split())
l=[]
c=1
while 1:
    for _ in range(c):l.append(c)
    if len(l) >= b:break
    c+=1
print(sum(l[a-1:b]))