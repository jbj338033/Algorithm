cnt = 1

for i in range(1, int(input())+1):
    cnt *= i
    cnt = int(str(cnt).rstrip("0")[-12:])

print(str(cnt)[-5:])