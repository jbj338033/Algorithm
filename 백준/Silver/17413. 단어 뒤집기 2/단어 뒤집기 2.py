s=input()

ignore=False
word=''

for i in s:
    if i=='<':
        ignore=True
        print(word[::-1],end='')
        word=''
        print(i,end='')
    elif i=='>':
        ignore=False
        print(i,end='')
    elif ignore:
        print(i,end='')
    elif i==' ':
        print(word[::-1],end=' ')
        word=''
    else:
        word += i
print(word[::-1])