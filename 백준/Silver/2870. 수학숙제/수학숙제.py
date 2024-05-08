p=[]
for _ in range(int(input())):
    s=input()
    n=''
    for i in s:
        if i.isdigit():
            n+=i
        else:
            if n:
                p.append(int(n))
                n=''
    if n:
        p.append(int(n))
p.sort()
print(*p,sep='\n')