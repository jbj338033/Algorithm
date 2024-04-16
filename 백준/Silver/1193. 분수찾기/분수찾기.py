x,l=int(input()),1
while x > l:
    x -= l
    l += 1
print(f'{x}/{l-x+1}' if l%2==0 else f'{l-x+1}/{x}')