l, r = 0, 100000000000
a = [0] * 1000001
k = int(input())
a[1] = 1
for i in range(1, 1000001):
    if a[i]:
        for j in range(i * 2, 1000001, i):
            a[j] -= a[i]
while l < r - 1:
    m = (l + r) // 2
    p = 0
    for i in range(1, int(m**0.5) + 1):
        p += a[i] * (m // (i * i))
    if m - p < k:
        l = m
    else:
        r = m
print(r)
