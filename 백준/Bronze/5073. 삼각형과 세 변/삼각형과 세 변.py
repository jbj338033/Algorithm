while 1:
    a,b,c=map(int,input().split())
    if a==b==c==0: break

    l=[a,b,c]
    m=max(l)
    l.remove(m)
    if sum(l) <= m:
        print("Invalid")
        continue

    if a==b==c:print("Equilateral")
    elif a==b or a==c or b==c:print("Isosceles")
    else:print("Scalene")