for _ in range(int(input())):
    s=[]
    for i in input():
        if i=='(':
            s.append(i)
        else:
            if s:
                s.pop()
            else:
                print('NO')
                break
    else:
        print('NO' if s else 'YES')