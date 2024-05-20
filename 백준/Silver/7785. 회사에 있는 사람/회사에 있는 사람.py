s=set()
for _ in range(int(input())):
    n,m=input().split()
    if m=='enter':s.add(n)
    else:s.remove(n)
print(*sorted(s,reverse=True),sep='\n')