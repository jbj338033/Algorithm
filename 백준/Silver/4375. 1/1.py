while 1:
    try:
        n=int(input())
        i='1'
        c=1
        while int(i)%n!=0:
            i+='1'
            c+=1
        print(c)
    except:break