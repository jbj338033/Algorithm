import sys
a=bytearray(2**22)
s=''
while True:
    c=sys.stdin.read(1)
    if c.isnumeric():s+=c
    else:
        n=int(s)
        d=n//8
        r=n%8
        if not a[d]&(1<<r) :
            print(n,end=' ')
            a[d]|=1<<r
        s=''
        if c != ' ':break