input()
dic={}
for i in map(int,input().split()):
    dic[i]=dic.get(i,0)+1
n=int(input())

for i in map(int,input().split()):
    print(dic.get(i,0),end=' ')