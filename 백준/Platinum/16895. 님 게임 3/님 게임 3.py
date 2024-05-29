import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
t=0
for i in l:t^=i
if t==0:print(0)
elif len(l)==1:print(1)
else:
    c=0
    for i in range(len(l)):
        if t^l[i]<=l[i]:c+=1
    print(c)