n=int(input())
l=[tuple(map(int,input().split())) for _ in range(n)]
l.sort(key=lambda x:(x[1],x[0]))
a=0
c=0
for i in l:
    if i[0]>=a:
        a=i[1]
        c+=1
print(c)