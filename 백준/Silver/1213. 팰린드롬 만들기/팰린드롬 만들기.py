s=input()
l=[0]*26
for i in s:l[ord(i)-65]+=1
o=0
c=''
e=''
for i in range(26):
    if l[i]%2==1:
        o+=1
        c=chr(i+65)
    e+=chr(i+65)*(l[i]//2)
print("I'm Sorry Hansoo"if o>1 else e+c+e[::-1])