for _ in range(int(input())):
  i = input().split()
  r = int(i[0])
  s = i[1]
  p = ""

  for i in range(len(s)):
    p += s[i] * r
  
  print(p)