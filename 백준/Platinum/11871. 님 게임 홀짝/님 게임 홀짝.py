n=int(input())
l=list(map(int,input().split()))
def grundy(n: int)-> int:
    return (n+1)//2 if n%2==1 else (n-2)//2
x=0
for i in l:x^=grundy(i)
print("cubelover" if x == 0 else "koosaga")