import sys
sys.stdin = open('input.txt', 'r')

def preorder(root):
    if root:
        print(root, end=' ')
        preorder(ch1[root])
        preorder(ch2[root])

T = int(input())
V = int(input())
arr = list(map(int, input().split()))
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

# 짝수 인덱스, 홀수 인덱스
# 완전 이진 트리
# 간선 수 = 노드 수 - 1
E = V - 1
for i in range(E):
    a = arr[2*i]         # 부모
    b = arr[2*i+1]       # 자식
    if ch1[a] == 0:
        ch1[a] = b
    else:
        ch2[a] = b

print(f'#{T}', end=' ')
preorder(1)