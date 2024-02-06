n, m = map(int, input().split())

a = set()
b = set()

for _ in range(n):
      a.add(input())

for _ in range(m):
      b.add(input())

l = sorted(list(a & b))

print(len(l))
print(*l, sep="\n")