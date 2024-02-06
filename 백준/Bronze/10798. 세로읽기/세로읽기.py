arr = ["" for _ in range(5)]

for i in range(5):
  arr[i] = input()

for i in range(15):
  for j in arr:
    try:
        print(j[i], end="")
    except:
       continue