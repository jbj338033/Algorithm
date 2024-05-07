s=0
for _ in range(int(input())):
    s+=1 if int(input()) else -1
print('Junhee is not cute!' if s<0 else 'Junhee is cute!')