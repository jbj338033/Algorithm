import sys
l=[]
for _ in range(int(sys.stdin.readline())):l.append(int(sys.stdin.readline()))
l.sort()
print(*l,sep='\n')