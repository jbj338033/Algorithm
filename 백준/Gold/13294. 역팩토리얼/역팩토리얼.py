import sys
import math
nfac = int(input())

l = 1
r = 1000000

while(l <= r):
    mid = (l + r) // 2
    res = math.factorial(mid)
    if(res == nfac):
        print(mid)
        sys.exit(0)
    elif(res < nfac):
        l = mid + 1
    else:
        r = mid - 1