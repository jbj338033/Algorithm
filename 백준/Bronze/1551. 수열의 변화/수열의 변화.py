n,k=map(int,input().split())
a=list(map(int,input().split(',')))
for i in range(k):
    a=[a[j+1]-a[j] for j in range(len(a)-1)]
print(','.join(map(str,a)))