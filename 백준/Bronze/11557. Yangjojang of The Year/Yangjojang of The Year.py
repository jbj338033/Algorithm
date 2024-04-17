for _ in range(int(input())):
    l=[]
    for _ in range(int(input())):
        a,b=input().split()
        l.append((a,int(b)))
    l.sort(key=lambda x: x[1])
    print(l[-1][0])