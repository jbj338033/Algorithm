# 7568 boj

n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
r=[]
for i in l:
    c=1
    for j in l:
        if i[0]<j[0] and i[1]<j[1]:c+=1
    r.append(c)
print(*r)
