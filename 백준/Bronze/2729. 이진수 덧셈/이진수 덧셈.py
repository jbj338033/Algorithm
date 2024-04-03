for _ in range(int(input())):
    a,b=map(lambda x: int(x,2),input().split())
    print(str(bin(a+b))[2:])