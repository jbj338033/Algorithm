import sys
input=sys.stdin.readline
n=1000001
l=[1]*n
for i in range(3,int(n**0.5)+1,2):
    if l[i]:
        for j in range(i*2,n,i):l[j]=0
while 1:
    n=int(input())
    if not n:break
    for i in range(3,int(n/2)+1,2):
        if l[i] and l[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
    else:print("Goldbach's conjecture is wrong.")