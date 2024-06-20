from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a):
    n = len(a)
    m = len(a[0])
    b = deepcopy(a)
    q = deque()
    for i in range(n):
        for j in range(m):
            if b[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
                b[nx][ny] = 2
                q.append((nx, ny))
    c = 0
    for i in b:
        c += i.count(0)
    return c


r = 0

for walls in combinations(range(n * m), 3):
    ok = True
    for w in walls:
        if a[w // m][w % m] != 0:
            ok = False
            break
    if not ok:
        continue
    b = deepcopy(a)
    for w in walls:
        b[w // m][w % m] = 1
    r = max(r, bfs(b))

print(r)
