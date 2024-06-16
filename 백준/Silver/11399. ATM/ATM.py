import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()
s = 0

for i in range(n):
    s += p[i] * (n - i)

print(s)
