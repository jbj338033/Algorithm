n=int(input())
l=list(map(int,input().split()))
r=0
for i in l:
    r^=0 if i<4 else 1 if i<16 else 2 if i<82 else 0 if i<6724 else 3 if i<50626 else 1 if i<2562991876 else 2
print('koosaga' if r else 'cubelover')