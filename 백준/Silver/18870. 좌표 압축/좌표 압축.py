import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
s = sorted(set(l))
d = {s[i]: i for i in range(len(s))}
print(*[d[i] for i in l])
