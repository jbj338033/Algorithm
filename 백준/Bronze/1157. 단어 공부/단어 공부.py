s = input().upper()
l = list(set(s))
c = []

for i in l:
    c.append(s.count(i))

if (c.count(max(c))) >= 2:
    print("?")
else:
    print(l[c.index(max(c))])