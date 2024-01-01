from sys import stdin

n, m = map(int, input().split())

l = [i for i in range(1, n +1)]

for _ in range(m):
    i, j = map(int, stdin.readline().split())

    for a in range((j - i) // 2 + 1):
        b = i + a - 1
        c = j - a - 1

        tmp = l[b]
        l[b] = l[c]
        l[c] = tmp

print(" ".join(map(str, l)))
