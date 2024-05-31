def f(s):
    n=0
    for i in s:
        try:
            n+=int(i)
        except:continue
    return n
l=[input() for _ in range(int(input()))]
l.sort(key=lambda x:(len(x),f(x),x))
print(*l,sep='\n')