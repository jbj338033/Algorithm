l=[]
c=0
while 1:
    try:
        for i in input().split():
            if c==0:
                c+=1
                continue
            l.append(int(i[::-1]))
    except:break
l.sort()
for i in l:
    print(i)