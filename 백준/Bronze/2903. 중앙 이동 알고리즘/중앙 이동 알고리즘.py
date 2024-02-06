n = int(input())
cnt = 2

for i in range(n):
    cnt += cnt - 1

print(cnt * cnt)