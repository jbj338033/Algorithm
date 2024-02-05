import sys

l = list()

for i in range(10):
  l.append(int(sys.stdin.readline()) % 42)

print(len(set(l)))