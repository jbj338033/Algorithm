s=sorted(map(int,input().split()))
print(s[0]+s[1]+min(s[2],s[0]+s[1]-1))