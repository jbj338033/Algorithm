import sys
for i in range(int(input())):
    s=sys.stdin.readline().split()
    print(f'Case #{i+1}:',end=' ')
    for j in reversed(s):
        print(j,end=' ')
    print()