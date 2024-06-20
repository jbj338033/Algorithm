a, b = map(int, input().split())

r = 1
while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        print(-1)
        exit()
    r += 1
if a != b:
    print(-1)
else:
    print(r)
