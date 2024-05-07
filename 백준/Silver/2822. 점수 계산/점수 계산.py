l=[]
for i in range(1,9):
    l.append((int(input()),i))
l.sort(reverse=True)
l=l[:5]
print(sum(i[0] for i in l))
print(*[i[1] for i in sorted(l,key=lambda x:x[1])])