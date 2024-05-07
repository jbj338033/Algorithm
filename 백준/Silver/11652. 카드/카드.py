import sys
input=sys.stdin.readline
n=int(input())
d={}
for i in range(n) :
    c=int(input())
    if c in d :
        d[c]+=1
    else :
        d[c]=1
result = sorted(d.items(),key=lambda x:(-x[1],x[0]))
print(result[0][0])