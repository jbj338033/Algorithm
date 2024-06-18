min, max = map(int, input().split())
l = [0] * (max - min + 1)
c = 0
for i in range(2, int(max**0.5) + 1):
    z = i**2
    s = (min // z) * z
    if s < min:
        s += z
    for j in range(s, max + 1, z):
        if not l[j - min]:
            l[j - min] = 1
            c += 1
print(max - min - c + 1)
