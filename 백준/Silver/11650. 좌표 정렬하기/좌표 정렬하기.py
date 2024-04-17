import sys
l=[]
for _ in range(int(input())):
    x,y=map(int,sys.stdin.readline().split())
    l.append((x,y))
l.sort()
for i in l:
    print(i[0],i[1])