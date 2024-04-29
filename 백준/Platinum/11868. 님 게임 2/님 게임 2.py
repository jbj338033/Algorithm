n=int(input())
p=list(map(int,input().split()))

if n==1:print('koosaga')
else:
    a=0
    for i in p:a^=i
    print('koosaga' if a else 'cubelover')