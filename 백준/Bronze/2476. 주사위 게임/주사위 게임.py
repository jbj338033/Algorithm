s=[]
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    
    if a==b==c:
        s.append(10000 + a*1000)
    elif a==b or a==c:
        s.append(1000 + a*100)
    elif b==c:
        s.append(1000 + b*100)
    else:
        s.append(max(a,b,c) * 100)
print(max(s))