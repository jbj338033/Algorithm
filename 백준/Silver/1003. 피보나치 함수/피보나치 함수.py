import sys

for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    
    a,b=1,0
    for _ in range(n):
        a,b=b,a+b
    print(a,b)