s=0
m=0
for _ in range(10):
    a,b=map(int,input().split())
    s-=a
    s+=b
    if s>m:
        m=s
print(m)