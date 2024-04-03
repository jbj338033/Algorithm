import sys
l=[]
for _ in range(int(input())):
    i=sys.stdin.readline().split()
    a=int(i[0])
    n=i[1]

    l.append((a,n))
l.sort(key=lambda x: x[0])
for i in l:
    print(i[0],i[1])