h, m = map(int, input().split())
t = int(input())

m += t

h += m // 60
m %= 60

h %= 24

print(h, m)