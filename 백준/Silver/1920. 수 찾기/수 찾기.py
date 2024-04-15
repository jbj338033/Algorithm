import sys
i=sys.stdin.readline
i()
a=set(map(int,i().split()))
i()
for b in map(int,i().split()):
    print(1 if b in a else 0)