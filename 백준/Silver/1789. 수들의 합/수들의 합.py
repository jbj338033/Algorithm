s=int(input())
a=0
i=1
while 1:
    a+=i
    if a>s:
        b=i
        break
    i+=1
print(b-1)