import math

m=int(input())
n=int(input())
s=0
min=10001
for i in range(m,n+1):
    if math.isqrt(i)**2==i:
        s+=i
        if i<min:
            min=i
if s==0:
    print(-1)
else:
    print(s)
    print(min)