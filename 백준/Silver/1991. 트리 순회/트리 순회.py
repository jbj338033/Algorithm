import sys
input=sys.stdin.readline
n=int(input())
tree={}
for i in range(n):
    a,b,c=input().split()
    tree[a]=[b,c]
def preorder(r):
    if r!='.':
        print(r,end='')
        preorder(tree[r][0])
        preorder(tree[r][1])
def inorder(r):
    if r!='.':
        inorder(tree[r][0])
        print(r,end='')
        inorder(tree[r][1])
def postorder(r):
    if r!='.':
        postorder(tree[r][0])
        postorder(tree[r][1])
        print(r,end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')