def p(c):
    if c in '()': return 0
    if c in '+-':return 1
    if c in '*/':return 2
    return -1
s=[]
l=[]
for i in input():
    if i=='(':s.append(i)
    elif i==')':
        while s:
            o=s.pop()
            if o=='(':break
            l.append(o)
    elif i in '+-*/':
        while s:
            o=s[-1]
            if p(i)<=p(o):
                l.append(o)
                s.pop()
            else:break
        s.append(i)
    else:l.append(i)
while s:l.append(s.pop())
print(*l, sep='')