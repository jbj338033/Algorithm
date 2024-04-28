while 1:
    a,b,c=input().split()
    b,c=int(b),int(c)
    if a=='#':break
    print(a,end=' ')
    if b>17 or c>=80:
        print('Senior')
    else:
        print('Junior')