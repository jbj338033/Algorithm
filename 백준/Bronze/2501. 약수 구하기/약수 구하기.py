n, k = map(int, input().split())
arr = [i for i in range(1, n+1) if n % i == 0]

if len(arr) < k:
    print(0)
else:
    print(sorted(arr)[k-1])