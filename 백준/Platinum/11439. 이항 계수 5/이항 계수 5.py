n, k, m = map(int, input().split())
nk = n - k

pl = [2, 3]
for i in range(5, n + 1, 2):
    f = 0
    for j in pl:
        if j**2 > i:
            break
        if i % j == 0:
            f = 1
            break

    if not f:
        pl.append(i)

d1, d2, d3 = {}, {}, {}


def c(n, d):
    for i in pl:
        p = i
        while p <= n:
            d[i] = d.get(i, 0) + n // p
            p *= i


c(n, d1)
c(nk, d2)
c(k, d3)

d4 = {}
for k, v in d1.items():
    e = d1[k] - d2.get(k, 0) - d3.get(k, 0)
    if e == 0:
        continue
    else:
        d4[k] = e


def pow(n, k, m):
    if k == 1:
        return n
    h = pow(n, k // 2, m)
    if k % 2 == 0:
        return (h**2) % m
    else:
        return (h**2 * n) % m


r = 1
for k, v in d4.items():
    r *= pow(k, v, m)
    r %= m

print(r)
