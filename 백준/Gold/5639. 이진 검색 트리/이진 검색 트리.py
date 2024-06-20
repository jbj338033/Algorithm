import sys

sys.setrecursionlimit(10**6)

l = []
while 1:
    try:
        l.append(int(input()))
    except:
        break


def f(s, e):
    if s > e:
        return
    m = e + 1
    for i in range(s + 1, e + 1):
        if l[i] > l[s]:
            m = i
            break
    f(s + 1, m - 1)
    f(m, e)
    print(l[s])


f(0, len(l) - 1)
