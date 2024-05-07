l=[]
for _ in range(int(input())):
    n,d,m,y=input().split()
    l.append((n,int(d),int(m),int(y)))
l.sort(key=lambda x:(x[3],x[2],x[1]))
print(l[-1][0])
print(l[0][0])