# a,b,c=map(int,input().split())
# r=1
# while b:
#     if b&1:r*=a
#     a*=a
#     b>>=1
# print(a%c)
a,b,c=map(int,input().split())
print(pow(a,b,c))