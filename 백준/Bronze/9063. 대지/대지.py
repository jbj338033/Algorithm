n=int(input())
xl,yl=[],[]
for _ in range(n):
    x,y=map(int,input().split())
    xl.append(x)
    yl.append(y)
print((max(xl)-min(xl))*(max(yl)-min(yl)))