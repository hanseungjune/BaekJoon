import sys
sys.stdin = open('input.txt','r')

T = int(input())
arr = [[0] * 100 for _ in range(100)]

for tc in range(1, T+1):
    left, bottom = map(int, input().split())

    for i in range(bottom, bottom+10):
        for j in range(left, left+10):
            arr[i][j] = 1

    sum_n = 0
    for l in range(100):
        for k in range(100):
            sum_n += arr[l][k]

print(sum_n)