l=int(input())
s=input()
sl=len(s)
p=[0 for _ in range(sl)]
j=0
for i in range(1,sl):
    while j>0 and s[i]!=s[j]:
        j=p[j-1]
    if s[i]==s[j]:
        j+=1
        p[i]=j
print(sl-p[sl-1])