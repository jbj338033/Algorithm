for _ in range(3):
    n=list(map(int,input().split())).count(0)
    print('E' if n==0 else 'A' if n==1 else 'B' if n==2 else 'C' if n==3 else 'D')