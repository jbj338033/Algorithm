from itertools import combinations_with_replacement

n, m = map(int, input().split())
a = list(map(int, input().split()))

for c in combinations_with_replacement(sorted(set(a)), m):
    print(*c)
