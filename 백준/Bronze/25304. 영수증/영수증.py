import sys

x = int(input())
n = int(input())

r = 0

for i in range(n):
  a, b = map(int, sys.stdin.readline().split())

  r += a * b

if x == r:
  print("Yes")
else:
  print("No")