import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = a[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + a[i][0]
    dp[i][i] = dp[i - 1][i - 1] + a[i][i]

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + a[i][j]

print(max(dp[n - 1]))
