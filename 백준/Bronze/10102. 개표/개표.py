input()
s=0
for i in input():
    s+=1 if i=='A' else -1
print('A' if s>0 else 'B' if s<0 else 'Tie')