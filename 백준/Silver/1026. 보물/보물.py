input()
a,b=sorted(map(int,input().split())),sorted(map(int,input().split()),reverse=True)
print(sum([a[i]*b[i] for i in range(len(a))]))