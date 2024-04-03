import sys
n,m=map(int,input().split())
l = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    lx,ly,rx,ry=map(int,sys.stdin.readline().split())
    for x in range(lx-1, rx):
        for y in range(ly-1, ry):
            l[y][x] += 1
c=0
for i in l:
    for j in i:
        if j>m:c += 1
print(c)