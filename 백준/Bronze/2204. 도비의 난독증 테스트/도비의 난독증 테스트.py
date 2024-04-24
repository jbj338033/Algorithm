while 1:
    n=int(input())
    if n==0:break
    l=[]
    for _ in range(n):
        a=input()
        l.append((a.lower(), a))
    l.sort(key=lambda x:x[0])
    print(l[0][1])
    l=[]