for i in range(int(input())):
    a,b,c=map(int,input().split())
    print(f'Scenario #{i+1}:')
    m=max(a,b,c)
    if m==a:
        if a**2==b**2+c**2:
            print('yes')
        else:
            print('no')
    elif m==b:
        if b**2==a**2+c**2:
            print('yes')
        else:
            print('no')
    else:
        if c**2==a**2+b**2:
            print('yes')
        else:
            print('no')
    print()