n = 13
N = n
H = 0

while n >= 1:
    n //= 2
    H += 1

tree = [0]*(2**(H+1))
tree[1] = 1
data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
for i in range(N-1):
    parent = tree.index(data[i*2])
    if tree[parent*2]:
        tree[parent*2+1] = data[i*2+1]
    else:
        tree[parent*2] = data[i*2+1]
# 루트노드에서 시작해서 순회하는 함수
# 루트노드를 인자로 받음(노드의 인덱스를 인자로 받음)
# n: 현재노드
def preorder(n):
    # n이 tree 의 인덱스를 벗어나면, 순회 그만!
    # n이 가리키는 인덱스의 값이 0이면,노드가 없음! 순회그만!
    if n >= 2**(H+1) or tree[n] == 0:
        return
    print(tree[n], end=' ')
    preorder(n*2)
    preorder(n*2+1)

preorder(1)