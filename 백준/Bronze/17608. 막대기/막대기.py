import sys
s=[]
for i in range(int(input())):
    s.append(int(sys.stdin.readline()))
c=0
m=0
for i in reversed(s):
    if i>m:
        c+=1
        m=i
    else:continue
print(c)