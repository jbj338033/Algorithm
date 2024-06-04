def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True
for _ in range(int(input())):
    n=int(input())
    a,b=n//2,n//2
    while a>0:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        a-=1
        b+=1