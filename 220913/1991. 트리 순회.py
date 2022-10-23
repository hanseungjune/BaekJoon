import sys
sys.stdin = open('input.txt', 'r')

V = int(input())
tree = {}
# print(tree)

for j in range(1, V+1):
    node, left, right = input().split()
    tree[node] = [left, right]
# print(tree)
root = 'A'

def preorder(root):
    if root == '.':
        return
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
    if root == '.':
        return
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

def postorder(root):
    if root == '.':
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')

preorder(root)
print()
inorder(root)
print()
postorder(root)