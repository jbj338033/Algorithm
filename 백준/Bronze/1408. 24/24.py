h1,m1,s1=map(int,input().split(':'))
h2,m2,s2=map(int,input().split(':'))
h3=h2-h1
m3=m2-m1
if m3<0:
    h3-=1
    m3+=60
s3=s2-s1
if s3<0:
    m3-=1
    s3+=60
    if m3<0:
        h3-=1
        m3+=60
h3=(h3+24)%24
print('%02d:%02d:%02d'%(h3,m3,s3))