from itertools import permutations

n, m = map(int, input().split())
a = list(map(int, input().split()))

for p in sorted(set(permutations(a, m))):
    print(*p)
