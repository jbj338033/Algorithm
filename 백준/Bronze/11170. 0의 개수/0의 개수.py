for _ in range(int(input())):
    n,m=map(int,input().split())
    s=0
    for i in range(n,m+1):
        s+=str(i).count('0')
    print(s)