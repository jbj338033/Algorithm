a,b=map(int, input().split())
print(a//b,end = '')
if a%b:
    print('.',end='')
    i=0
    while a%b and i<1000: 
        a=a%b*10 # 계속 10씩 곱해주면서 몫을 뒤에 붙여줌 
        i+=1
        print(a//b,end='')