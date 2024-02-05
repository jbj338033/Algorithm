n = int(input())
m = (n * 2 - 1)

for i in range(1, m, 2):
    s="*"*i
    print(f"{s: ^{m}}".rstrip())
print("*"*m)
for i in range(m-2, 0, -2):
    s="*"*i
    print(f"{s: ^{m}}".rstrip())