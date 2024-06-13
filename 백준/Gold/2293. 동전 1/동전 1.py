n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]
dp=[0]*(k+1)
dp[0]=1
for i in a:
    for j in range(i,k+1):
        dp[j]+=dp[j-i]
print(dp[k])