import sys

def preorder(tree, node):
    if node != '.':
        result1.append(node)
    if node != '.':
        preorder(tree, tree[node][0])
    if node != '.':
        preorder(tree, tree[node][1])

def inorder(tree, node):
    if node != '.':
        inorder(tree, tree[node][0])
    if node != '.':
        result2.append(node)
    if node != '.':
        inorder(tree, tree[node][1])

def postorder(tree, node):
    if node != '.':
        postorder(tree, tree[node][0])
    if node != '.':
        postorder(tree, tree[node][1])
    if node != '.':
        result3.append(node)

N = int(input())
tree = {}
result1= []
result2=[]
result3=[]
for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)
preorder(tree, 'A')
for i in result1:
    print(i, end="")
print()
inorder(tree, 'A')
for i in result2:
    print(i, end="")
print()
postorder(tree, 'A')
for i in result3:
    print(i, end="")
