import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 목표 : 재귀로 풀기
def dfs(S, T):
    global answer
    # 길이는 같을수 있으나, 모양이 다를수 있음
    # 2가지 경우로 재귀할 수 있다..?
    if len(T) < len(S):
        return

    if T == S:
        answer = True
        return
    if T[0] == 'B':
        dfs(S, T[::-1][:-1])
    if T[-1] == 'A':
        dfs(S, T[:-1])

# 바꿔야하는 문자열
S = input().rstrip()
# 변경해야하는 문자열
T = input().rstrip()
# S를 T로 바꾸는거보다 T를 S로 바꾸는게 경우의 수가 더 적다라고 판단
# 기본적으로는 False인데, 만약 같아지는게 가능하면 True로 바꿀예정

answer = 0
dfs(S, T)
if answer:
    print(1)
else:
    print(0)
