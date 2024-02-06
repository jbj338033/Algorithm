import sys

arr = []

for _ in range(int(input())):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(*arr, sep="\n")