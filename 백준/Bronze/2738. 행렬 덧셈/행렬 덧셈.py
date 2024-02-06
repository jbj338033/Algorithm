n, m = map(int, input().split())

a = [[0 for _ in range(m)] for _ in range(n)]
b = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    a[i] = l

for i in range(n):
    l = list(map(int, input().split()))
    b[i] = l

for i in range(n):
    print(*[a[i][j] + b[i][j] for j in range(m)])