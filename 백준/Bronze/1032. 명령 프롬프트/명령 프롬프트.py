n=int(input())
s=list(input())
for _ in range(n-1):
    a=input()
    for i in range(len(a)):
        if s[i] != a[i]:s[i] = "?"
print(*s,sep='')