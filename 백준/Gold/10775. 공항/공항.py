import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

g = int(input())
p = int(input())

o = []

for i in range(g + 1):
    o.append(i)


def f(n):
    if n == o[n]:
        return n
    o[n] = f(o[n])
    return o[n]


l = [int(input()) for _ in range(p)]
s = 0

for p in l:
    r = f(p)
    if r == 0:
        break
    o[r] = r - 1
    s += 1

print(s)
