while 1:
    a=input()
    l=[]
    if a == ".":break
    for i in a:
        if i=='[' or i=='(':l.append(i)
        elif i == ']':
            if l and l[-1]=='[':l.pop()
            else:
                l.append(']')
                break
        elif i==')':
            if l and l[-1]=='(':l.pop()
            else:
                l.append(')')
                break
    print('no' if l else 'yes')