a=input().split('.')
s=''
for i in a:
    l=len(i)
    if l%2!=0:
        print(-1)
        exit()
    if l%4==2 or l%4==0:
        s+='AAAA'*(l//4)
        i=i[l//4*4:]
        l=len(i)
    if l%2==0:
        s+='BB'*(l//2)
        i=i[l//2*2:]
    s+='.'
print(s[:-1])