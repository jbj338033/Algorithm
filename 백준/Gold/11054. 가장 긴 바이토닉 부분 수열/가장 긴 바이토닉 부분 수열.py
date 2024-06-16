import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if l[i]>l[j]:dp[i]=max(dp[i],dp[j]+1)
        else:dp[i]=max(dp[i],1)
dp2=[1]*n
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if l[i]>l[j]:dp2[i]=max(dp2[i],dp2[j]+1)
        else:dp2[i]=max(dp2[i],1)
r=0
for i in range(n):
    r=max(r,dp[i]+dp2[i])
print(r-1)