l=[]
while 1:
    try:
        l.append(int(input()))
    except:
        break
print(sum(l)//len(l))
h=(0,0)
for i in set(l):
    if l.count(i)>h[1]:
        h=(i,l.count(i))
print(h[0])