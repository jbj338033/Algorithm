for _ in range(int(input())):
    n=list(map(int,input().split()))
    n.remove(min(n))
    n.remove(max(n))
    if max(n) - min(n) >= 4:
        print('KIN')
    else:
        print(sum(n))