arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            arr[i][j] = 1

cnt = 0

for a in arr:
    cnt += a.count(1)

print(cnt)