from sys import stdin

arr = [0] * 10001

for i in range(int(stdin.readline())):
    arr[int(stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)