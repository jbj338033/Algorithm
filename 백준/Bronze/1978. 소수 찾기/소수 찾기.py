input()

l = map(int, input().split())
cnt = 0

for i in l:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                cnt += 1
            break

print(cnt)