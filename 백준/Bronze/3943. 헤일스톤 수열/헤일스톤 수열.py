import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    m=1
    while 1:
        if n>m:m=n
        if n==1:break
        if n%2:n=n*3+1
        else:n//=2
    print(m)