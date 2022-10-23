# 3중 반복으로 3가지 카드 뽑는 경우의 수 구하기 ( 중복 안됨 )

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()

choice = []
for i in card:
    for j in card:
        if i != j:
            for k in card:
                if i != k and j != k:
                    choice.append((i, j, k))
                    
# print(choice)
for i in range(len(choice)):
    choice[i] = sum(choice[i])
choice.sort()

answer = []
for j in choice:
    if j <= M:
        answer.append(j)
answer.sort()

print(answer[-1])
    
