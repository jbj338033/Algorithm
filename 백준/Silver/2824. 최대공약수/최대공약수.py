import math

input()
n = 1
for i in map(int, input().split()):
    n *= i
input()
m = 1
for i in map(int, input().split()):
    m *= i
print(str(math.gcd(n, m))[-9:])
