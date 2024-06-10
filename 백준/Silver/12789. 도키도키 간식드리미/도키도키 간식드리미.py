n=int(input())
l=list(map(int,input().split())) 
s=[]
c=1
for i in l:
    s.append(i)
    while s and s[-1]==c:
        s.pop()
        c+=1
print('Sad' if s else 'Nice')