n, x = map(int, input().split())
print(" ".join(map(str, filter(lambda a: a < x, list(map(int, input().split()))))))