n=int(input())
for i in range(1,n+1):
    s = "*"*(i*2-1)
    print(s.center(n*2-1).rstrip())