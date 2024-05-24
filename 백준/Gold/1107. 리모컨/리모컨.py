import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
broken=list(map(int, input().split()))
b=abs(100-n)
for a in range(1000001):
    a=str(a)
    for j in range(len(a)):
        if int(a[j]) in broken:break
        elif j==len(a)-1:b=min(b,abs(int(a)-n)+len(a))
print(b)