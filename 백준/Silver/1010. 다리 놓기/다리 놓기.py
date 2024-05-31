import math    
for _ in range(int(input())):
    n,m=map(int,input().split())
    print(math.factorial(m)//(math.factorial(n)*math.factorial(m-n)))