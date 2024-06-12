n=int(input())
l=list(map(int,input().split()))
t,p=map(int,input().split())
r=0
for i in l:r+=(i+t-1)//t
print(r);print(n//p,n%p)