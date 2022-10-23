import sys
sys.stdin = open('input.txt', 'r')

L, C = map(int, input().split())
alpha = sorted(input().split())  # 1

# 조건에 해당하는 패스워드인지 확인하고 출력
def is_password(arr):
    vowel_cnt = 0
    for i in arr:
        if i in 'aeiou':
            vowel_cnt += 1
    if vowel_cnt>=1 and L - vowel_cnt>=2:
        print(''.join(arr))

# dfs를 통해서 L자리 암호 구하기(재귀 두번을 반복하면서 하나 지우고 그 다음 인덱스를 꺼내올수있음)
def dfs(idx, arr):
    if L == len(arr):
        is_password(arr)
        return
    if idx == C:
        return
    arr.append(alpha[idx])
    dfs(idx+1, arr)
    arr.pop()
    dfs(idx+1, arr)

dfs(0, [])