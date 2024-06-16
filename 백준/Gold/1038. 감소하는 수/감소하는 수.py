n=int(input())
if n>1022:
    print(-1)
    exit()
if n<10:
    print(n)
    exit()
q=[i for i in range(10)]
c=9
while c<n:
    x=q.pop(0)
    for i in range(x%10):
        q.append(x*10+i)
        c+=1
        if c==n:
            print(x*10+i)
            exit()
print(-1)