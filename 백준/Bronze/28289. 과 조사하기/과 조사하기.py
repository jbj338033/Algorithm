a,b,c,d=0,0,0,0
for i in range(int(input())):
    gp,cp,np=map(int,input().split())
    if gp == 1:d+=1
    else:
        if cp==1 or cp==2:a+=1
        elif cp==3:b+=1
        else:c+=1

print(a,b,c,d,sep='\n')