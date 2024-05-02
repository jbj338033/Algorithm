m=int(input())
d=int(input())

if m==2 and d==18:
    print('Special')
elif m<2:
    print('Before')
elif m==2 and d<18:
    print('Before')
else:
    print('After')