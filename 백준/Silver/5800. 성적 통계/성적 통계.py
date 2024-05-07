for i in range(1,int(input())+1):
    a=list(map(int,input().split()))[1:]

    print('Class',i)

    a.sort()
    gap=0
    for j in range(len(a)):
        if j==len(a)-1:break
        if a[j+1] - a[j] > gap:
            gap = a[j+1] - a[j]
    print(f'Max {max(a)}, Min {min(a)}, Largest gap {gap}')