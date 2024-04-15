a,b,n=map(int,input().split())
for _ in range(n):
    a=(a%b)*10
    r=a//b
print(r)