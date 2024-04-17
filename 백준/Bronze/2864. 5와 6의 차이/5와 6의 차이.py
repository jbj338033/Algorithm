i=input().split()
a1,b1=map(lambda x: int(x.replace('6', '5')),i)
a2,b2=map(lambda x: int(x.replace('5', '6')),i)
print(a1+b1,a2+b2)