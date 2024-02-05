total = 0

for _ in range(int(input())):
  a = input()
  isGroup = True
  used = []
  previous = ""

  for s in a:
    if previous == "":
      used.append(s)
    elif previous != s:
      if s in used:
        isGroup = False
        break
      else:
        used.append(s)
    
    previous = s

  if isGroup:
    total += 1

print(total)