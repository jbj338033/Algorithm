n = int(input())
l = [1,1,0,1,1]
for i in range(5,n+1):   
    l.append(0 if l[i-1]+l[i-3]+l[i-4]==3 else 1)

if l[n] == 1 :
    print("SK")
else :
    print("CY")