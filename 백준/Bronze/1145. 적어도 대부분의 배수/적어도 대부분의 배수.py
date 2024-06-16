l=list(map(int,input().split()))
i=1
while 1:
    c=0
    i+=1
    for n in l:
        if i%n==0:c+=1
    if c>=3:break
print(i)