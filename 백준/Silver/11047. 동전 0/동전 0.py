n,k=map(int,input().split())
l=[int(input()) for _ in range(n)]
c=0
for i in l[::-1]:
    c+=k//i
    k%=i
print(c)
