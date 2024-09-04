import sys
input=sys.stdin.readline
l=[]
for _ in range(int(input())):
    s=input().split()
    c=s[0]
    if c=='push':
        l.append(int(s[1]))
    elif c=='pop':
        print(l.pop() if l else -1)
    elif c=='size':
        print(len(l))
    elif c=='empty':
        print(0 if l else 1)
    else:
        print(l[-1] if l else -1)