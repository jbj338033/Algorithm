t=int(input())
a=t//300
t%=300

b=t//60
t%=60

c=t//10
t%=10

if t:
    print(-1)
else:
    print(a,b,c)