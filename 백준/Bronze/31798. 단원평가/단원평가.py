import math
l=list(map(int,input().split()))
i=l.index(0)
if i==0:
    print(l[2]**2 - l[1])
elif i==1:
    print(l[2]**2 - l[0])
else:
    print(math.isqrt(l[0]+l[1]))