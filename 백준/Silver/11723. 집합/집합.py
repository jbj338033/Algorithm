import sys
s=set()
for _ in range(int(input())):
    a=sys.stdin.readline().split()
    k=a[0]

    if k=='add':
        v=int(a[1])
        if not v in s:
            s.add(v)
    elif k=='remove':
        v=int(a[1])
        if v in s:
            s.remove(v)
    elif k=='check':
        print(1 if int(a[1]) in s else 0)
    elif k=='toggle':
        v=int(a[1])
        if v in s:
            s.remove(v)
        else:
            s.add(v)
    elif k=='all':
        s=set(range(1,21))
    else:
        s.clear()