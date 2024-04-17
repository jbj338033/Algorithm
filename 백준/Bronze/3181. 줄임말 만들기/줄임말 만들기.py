a=input().split()
l= ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

for i in range(len(a)):
    if i!=0 and a[i] in l:continue
    print(a[i][0].upper(),end='')