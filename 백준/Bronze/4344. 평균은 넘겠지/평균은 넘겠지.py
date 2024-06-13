import sys
input=sys.stdin.readline
c=int(input())
for _ in range(c):
    l=list(map(int, input().split()))
    n=l[0]
    l=l[1:]
    a=sum(l)/n
    c=0
    for i in l:
        if i>a:c+=1
    print(f'{c/n*100:.3f}%')

