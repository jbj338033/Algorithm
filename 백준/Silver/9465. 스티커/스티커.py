t = int(input())

for _ in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2] if i > 1 else 0) + a[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2] if i > 1 else 0) + a[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))
