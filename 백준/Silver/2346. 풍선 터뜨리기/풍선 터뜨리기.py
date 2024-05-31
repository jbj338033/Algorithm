from collections import deque
input()
q=deque(enumerate(map(int,input().split())))
while q:
    p=q.popleft()
    print(p[0]+1,end=' ')
    n=p[1]
    if n>0:
        q.rotate(-(n-1))
    else:
        q.rotate(-n)

# 3 2 1 -3 -1 -> 1 , 3

# 2 1 -3 -1
# -1 -3 1 2
# -3 1 2 -1 -> 4, -3

# -1 2 1
# 2 1 -1
# 1 -1 2
# -1 2 1 -> 5, -1

# 2 1
# 1 2 -> 3, 1

# 2
# 2 -> 2, 2

# 1 4 5 3 2