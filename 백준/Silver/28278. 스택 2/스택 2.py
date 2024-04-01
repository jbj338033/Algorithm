import sys
stack=[]
for _ in range(int(input())):
    s=sys.stdin.readline().split()
    c=int(s[0])
    
    if c == 1:
        stack.append(int(s[1]))
    elif c == 2:
        print(stack.pop() if stack else -1)
    elif c == 3:
        print(len(stack))
    elif c == 4:
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)