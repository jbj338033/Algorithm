n = int(input())
s=[]
r=[]
c=1
for i in range(n):
    n=int(input())
    while c<=n:
        s.append(c)
        r.append('+')
        c+=1
    if s[-1]==n:
        s.pop()
        r.append('-')
    else:
        print('NO')
        exit(0)
print(*r,sep='\n')