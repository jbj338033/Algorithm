def is_prime(n):
    for i in range(2, (n//2)+1):
        if n%i==0:return False
    return True
l=[]
for i in range(int(input()),int(input())+1):
    if i==1:continue
    if is_prime(i):
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(sum(l))
    print(min(l))