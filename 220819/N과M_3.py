answer = []
# N은 1~N의 자연수, M은 수열의 갯수(중복순열)
N, M = map(int, input().split())

def perm(idx, answer):
    if idx == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        answer.append(i)
        perm(idx+1, answer)
        answer.pop()

perm(0, answer)

