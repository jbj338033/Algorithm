s=set(range(1,10001))
q=set()
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    q.add(i)
d=sorted(s-q)
print(*d,sep='\n')