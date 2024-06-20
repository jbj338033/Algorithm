import sys

sys.setrecursionlimit(10**6)

n = int(input())
l = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

p = [0] * (n + 1)


def f(c, r):
    for i in l[c]:
        if i == r:
            continue
        p[i] = c
        f(i, c)


f(1, 0)

for i in range(2, n + 1):
    print(p[i])
