n=int(input())
a,b=1,1
for _ in range(1,n):
    a,b=b%1000000007,(a+b)%1000000007
print(a)