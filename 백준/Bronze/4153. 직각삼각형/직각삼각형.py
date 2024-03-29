while 1:
    a=list(map(int,input().split()))
    if a[0] == 0: break
    m=max(a)
    a.remove(m)

    if m**2 == a[0]**2 + a[1]**2:
        print("right")
    else: print("wrong")