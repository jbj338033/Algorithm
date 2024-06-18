def pow(n, k, m):
    if k == 1:
        return n
    h = pow(n, k // 2, m)
    if k % 2 == 0:
        return (h**2) % m
    else:
        return (h**2 * n) % m


n, k = map(int, input().split())

f = [1] * (n + 1)
for i in range(2, n + 1):
    f[i] = (f[i - 1] * i) % 1000000007


def i(n):
    return pow(f[n], 1000000005, 1000000007)


print(f[n] * i(n - k) * i(k) % 1000000007)
