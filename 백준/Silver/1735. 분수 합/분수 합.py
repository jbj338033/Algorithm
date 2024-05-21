import math
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())

l=math.lcm(b1,b2)
a1*=l//b1
a2*=l//b2
a=a1+a2
b=l
g=math.gcd(a,b)
print(a//g,b//g)
