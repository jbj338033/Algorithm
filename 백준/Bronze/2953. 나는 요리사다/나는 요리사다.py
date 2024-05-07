w=(0,0)
for i in range(5):
    s=sum(map(int,input().split()))
    if s>w[1]:
        w=(i+1,s)
print(*w)