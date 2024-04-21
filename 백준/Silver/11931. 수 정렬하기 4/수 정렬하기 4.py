import sys
l=[]
for _ in range(int(input())):l.append(int(sys.stdin.readline()))
l.sort(reverse=True)
print(*l,sep='\n')