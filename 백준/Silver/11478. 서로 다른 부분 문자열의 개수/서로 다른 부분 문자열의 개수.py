s=input()
l=len(s)
e=set()
for i in range(1,l+1):
    for j in range(l-i+1):
        e.add(s[j:j+i])
print(len(e))