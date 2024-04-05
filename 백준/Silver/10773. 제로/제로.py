import sys
s=[]
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    if n==0:s.pop()
    else:s.append(n)
print(sum(s))