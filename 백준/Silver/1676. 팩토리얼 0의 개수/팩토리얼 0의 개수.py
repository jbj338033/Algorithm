n=int(input())
for i in range(n-1,1,-1):
    n*=i
c=0
if n==0:print(0)
else:
    for i in str(n)[::-1]:
        if i=='0':c+=1
        else:break
    print(c)