n=int(input())
s=input()
r=0
for i in range(n):r+=((ord(s[i])-96)*(31**i))%1234567891
print(r%1234567891)