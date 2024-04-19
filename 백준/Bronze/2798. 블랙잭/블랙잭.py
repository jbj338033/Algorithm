n,m=map(int,input().split())
l=list(map(int,input().split()))

a=300001
t=0

for i in range(n-2):
    iv=l[i]
    for j in range(i+1,n-1):
        jv=l[j]
        for k in range(j+1,n):
            kv=l[k]
            mi=abs(m-iv-jv-kv)
            ti=iv+jv+kv

            if ti==m:
                print(ti)
                exit()

            if mi < a and ti <= m:
                a=mi
                t=ti
print(t)
