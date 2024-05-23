n=int(input())
a,b=1,1
if n==0:print(0)
elif n==1 or n==2:print(1)
else:
    for i in range(1,n):
        a,b=b,a+b
    print(a)