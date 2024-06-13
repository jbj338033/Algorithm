n=int(input())
l=list(map(int,input().split()))
g=[]
for i in l:
    s=str(i)
    a=len(s)
    while len(s)<10:s+=s[len(s)-a]
    g.append(([*s],str(i)))
g.sort(key=lambda x:x[0],reverse=True)
r=''
for i in g:r+=i[-1]
print(r if int(r)!=0 else 0)