a = input()
n = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
r = 0
for i in range(len(a)):
    for j in n:
        if a[i] in j:
            r += n.index(j) + 3
print(r)