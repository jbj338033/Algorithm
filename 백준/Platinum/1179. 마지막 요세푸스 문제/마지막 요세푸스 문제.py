n, k = map(int, input().split())
r = 0
c = 1
if k == 1:
    print(n)
else:
    while 1:
        a = (c - r - 1) // (k - 1) + 1
        if c + a > n:
            r += (n - c) * k
            break
        r = (r + k * a) % (c + a)
        c += a
    print(r+1)
