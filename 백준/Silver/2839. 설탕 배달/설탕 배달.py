n=int(input())
if n%5==0:print(n//5)
else:
    p=0
    while n>0:
        n-=3
        p+=1
        if n%5==0:
            p+=n//5
            print(p)
            break
        if n==1 or n==2:
            print(-1)
            break
        if n==0:
            print(p)
            break