for _ in range(int(input())):
    a,b=input().split()
    print('Distances:',end=' ')
    for i in range(len(a)):
        print((ord(b[i])-ord(a[i]))%26,end=' ')
    print()