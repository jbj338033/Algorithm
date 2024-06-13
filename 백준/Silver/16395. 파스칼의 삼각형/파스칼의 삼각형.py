n,k=map(int,input().split())
l=[[0]*k for _ in range(n)]
l[0][0]=1
for i in range(1,n):
    for j in range(k):
        if j==0:
            l[i][j]=1
        else:
            l[i][j]=l[i-1][j-1]+l[i-1][j]
print(l[n-1][k-1])