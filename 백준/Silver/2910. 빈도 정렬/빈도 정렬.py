n,c=map(int,input().split())
l=list(map(int,input().split()))
n=l[:]
l.sort(key=lambda x:(-n.count(x),n.index(x)))
print(*l)