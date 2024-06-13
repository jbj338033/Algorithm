l,r=map(str,input().split())
m=0
if len(l)!=len(r):print(0);exit()
for i in range(len(l)):
    if l[i]==r[i]:
        if l[i]=='8':m+=1
    else:break
print(m)