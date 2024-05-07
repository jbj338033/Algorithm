for _ in range(int(input())):
    a=input().split()
    n=float(a[0])
    for i in a[1:]:
        if i=='@':
            n*=3
        elif i=='%':
            n+=5
        elif i=='#':
            n-=7
    print('%.2f'%n)