import sys
input=sys.stdin.readline
n=int(input())
for h in range(1,10):
    for e in range(10):
        if h==e:continue
        for l in range(10):
            if l==h or l==e:continue
            for o in range(10):
                if o==h or o==e or o==l:continue
                else:hello=(10000*h+1000*e+100*l+10*l+o)
                for w in range(1,10):
                    if w==h or w==e or w==l or w==o:continue
                    for r in range(10):
                        if r==h or r==e or r==l or r==o or r==w:continue
                        for d in range(10):
                            if d==h or d==e or d==l or d==o or d==w or d==r:continue
                            else:world=(10000*w+1000*o+100*r+10*l+d)
                            helloworld=hello+world
                            if helloworld==n and n<100000:
                                print(f"  {hello}")
                                print(f"+ {world}")
                                print("-------")
                                print(f"  {n}")
                                sys.exit()
                            elif helloworld==n and n>=100000:
                                print(f"  {hello}")
                                print(f"+ {world}")
                                print("-------")
                                print(f' {n}')
                                sys.exit()
print("No Answer")