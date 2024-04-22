x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

x=x1 if x1!=x2 and x1!=x3 else x2 if x2!=x1 and x2!=x3 else x3
y=y1 if y1!=y2 and y1!=y3 else y2 if y2!=y1 and y2!=y3 else y3

print(x,y)