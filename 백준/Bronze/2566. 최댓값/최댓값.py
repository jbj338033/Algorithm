arr = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    arr[i] = list(map(int, input().split()))

m = max(map(max, arr))

print(m)
print(*[(i + 1, j + 1) for i in range(9) for j in range(9) if arr[i][j] == m][0])