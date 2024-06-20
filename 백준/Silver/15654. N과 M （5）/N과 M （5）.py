from itertools import permutations

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for p in permutations(a, m):
    print(*p)
