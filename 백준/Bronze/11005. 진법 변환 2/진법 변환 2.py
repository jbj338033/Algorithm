n, b = map(int, input().split())
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(n, b):
  q, r = divmod(n, b)

  if q == 0:
    return tmp[r]
  else:
    return convert(q, b) + tmp[r]

print(convert(n, b))