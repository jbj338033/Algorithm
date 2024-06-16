import sys
def f(x):
    for i in range(x):
        if l[x]==l[i] or abs(l[x]-l[i])==x-i:return False
    return True
def dfs(x):
    global r
    if x==n:r+=1
    else:
        for i in range(n):
            l[x]=i
            if f(x):dfs(x+1)
n=int(sys.stdin.readline())
l=[0]*n
r=0
dfs(0)
print(r)