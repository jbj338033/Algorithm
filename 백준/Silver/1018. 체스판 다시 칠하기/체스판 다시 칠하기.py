n,m=map(int,input().split())
l=[]
c=9999999
for _ in range(n):
    i=list(input())
    l.append(i)

wl=[
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
]

bl=[
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
]

for i in range(n-7):
    for j in range(m-7):
        nl=[]
        for k in range(i,i+8):
            nl.append(l[k][j:j+8])

        cca=0
        ccb=0
        for i2 in range(8):
            for j2 in range(8):
                if nl[i2][j2] != wl[i2][j2]:
                    cca+=1
        for i2 in range(8):
            for j2 in range(8):
                if nl[i2][j2] != bl[i2][j2]:
                    ccb+=1

        if c>cca or c>ccb:
            c=min(cca,ccb)
print(c)