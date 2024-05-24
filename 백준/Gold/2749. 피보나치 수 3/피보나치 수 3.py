n=int(input())%1500000
a,b=1,1
for i in range(n-1):
    a,b=b,(a+b)%1000000
print(a)