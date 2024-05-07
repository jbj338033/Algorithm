h,m,s=map(int,input().split())
n=int(input())

h+=n//3600
n%=3600

m+=n//60
n%=60

s+=n

m+=s//60
s%=60

h+=m//60
m%=60

h%=24

print(h,m,s)