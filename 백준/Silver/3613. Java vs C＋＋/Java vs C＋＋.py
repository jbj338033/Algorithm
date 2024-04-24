a=input()
r=''
if '__' in a or a[0].isupper() or ' ' in a or a[-1] == '_' or a[0] == '_':
    print('Error!')
elif '_' in a:
    q=0
    for i in a:
        if i.isupper():
            print('Error!')
            exit()
        if i=='_':
            q+=1
        elif q==1:
            q=0
            r+=i.upper()
        else:
            r+=i
# java
else:
    q=0
    for i in a:
        if i.isupper():
            r+='_'
            r+=i.lower()
        else:
            r+=i
print(r)