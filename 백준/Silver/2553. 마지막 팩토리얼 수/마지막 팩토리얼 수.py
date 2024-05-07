n=int(input())

for i in range(2,n):
    n*=i
for i in str(n)[::-1]:
    if i!='0':
        print(i)
        break