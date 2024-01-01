n, m = map(int, input().split())

l = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())

    # [::-1]
    l[i - 1:j] = l[i - 1:j][::-1]

# *l
print(*l)