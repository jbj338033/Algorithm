l=[]
for _ in range(int(input())):
    a=input().split()
    name=a[0]
    korean=int(a[1])
    english=int(a[2])
    math=int(a[3])
    l.append((name,korean,english,math))
l.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
print(*map(lambda x: x[0], l), sep='\n')