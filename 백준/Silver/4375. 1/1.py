while 1:
    try:
        n=int(input())
        i=1
        while 1:
            if int('1'*i)%n==0:
                print(i)
                break
            i+=1
    except:break