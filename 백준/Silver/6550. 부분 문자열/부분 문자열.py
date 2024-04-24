while 1:
    try:
        s,t=input().split()
        
        for i in s:
            if i in t:
                t=t[t.index(i)+1:]
            else:
                print('No')
                break
        else:
            print('Yes')
    except EOFError:
        break