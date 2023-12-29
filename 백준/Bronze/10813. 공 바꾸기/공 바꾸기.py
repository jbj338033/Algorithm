import sys

n, m = map(int, input().split())
l = [i + 1 for i in range(n)]

for i in range(m):
  i, j = map(int, sys.stdin.readline().split())

  i -= 1
  j -= 1

  tmp = l[i]
  l[i] = l[j]
  l[j] = tmp

print(" ".join(map(str, l)))