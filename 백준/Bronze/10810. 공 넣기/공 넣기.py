import sys

n, m = map(int, input().split())
l = [0 for _ in range(n)]

for _ in range(m):
  i, j, k = map(int, sys.stdin.readline().split())

  for a in range(i - 1, j):
    l[a] = k

print(" ".join(map(str, l)))