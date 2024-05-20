_,a,b=input(),set(map(int,input().split())),set(map(int,input().split()))
s=a-b
print(len(s))
if len(s):print(*sorted(s))