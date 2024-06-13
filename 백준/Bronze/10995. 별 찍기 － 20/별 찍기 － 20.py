n=int(input())

for i in range(n):
    print(f"{' ' if i%2==1 else ''}{'* '*n}")
