l=[int(input()) for _ in range(int(input()))]
s=[]
c=0
for i in l:
    while s and s[-1]<=i:s.pop()
    s.append(i)
    c+=len(s)-1
print(c)