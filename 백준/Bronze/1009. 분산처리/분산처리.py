for _ in range(int(input())):
    a,b=map(int,input().split())

    a = int(str(a)[-1])

    if a==0: print(10)
    elif a==1 or a==5 or a==6: print(a)
    elif a==2:
        i=b%4
        print(6 if i==0 else 2 if i==1 else 4 if i==2 else 8)
    elif a==3:
        i=b%4
        print(1 if i==0 else 3 if i==1 else 9 if i==2 else 7)
    elif a==4:
        if b%2==0: print(6)
        else: print(4)
    elif a==7:
        i = b%4
        print(1 if i==0 else 7 if i==1 else 9 if i==2 else 3)
    elif a==8:
        i=b%4
        print(6 if i==0 else 8 if i==1 else 4 if i==2 else 2)
    elif a==9:
        print(1 if b%2==0 else 9)