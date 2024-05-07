for _ in range(int(input())):
    a,b=input().split()
    a=int(a)
    b=list(b)
    del b[a-1]
    print(''.join(b))