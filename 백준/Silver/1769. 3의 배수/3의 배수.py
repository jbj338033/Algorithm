def f(n):
    if len(n)==1:return int(n)%3==0
    d=sum(int(i) for i in n)
    return f(str(d))
def c(n):
    c=0
    while len(n)>1:
        d=sum(int(i) for i in n)
        n=str(d)
        c+=1
    return c
n=input()
print(c(n))
if f(n):
    print("YES")
else:
    print("NO")