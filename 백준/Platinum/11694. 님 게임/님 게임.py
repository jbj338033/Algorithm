n=int(input())
x=0
f=0
for i in map(int,input().split()):
    x^=i
    f|=x>1
if f:
    print("koosaga" if x else "cubelover")
else:
    print("cubelover" if x else "koosaga")