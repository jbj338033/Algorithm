n=int(input())
heap=[0,1]
def swap(x,y):heap[x],heap[y]=heap[y],heap[x]
for i in range(2,n+1):
    heap.append(i)
    swap(i,i-1)
    j=i-1
    while j!=1:
        swap(j,j//2)
        j=j//2
for i in heap[1:]:
    print(i,end=' ')