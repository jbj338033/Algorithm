n = int(input())
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n):
    if i==0:continue
    print(' '*(n-i-1)+'*'*(2*i+1))