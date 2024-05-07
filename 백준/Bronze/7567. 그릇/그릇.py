p=''
s=0
for i in input():
    if p=='':
        p=i
        s+=10
    elif p==i:
        s+=5
    else:
        s+=10
        p=i
print(s)
