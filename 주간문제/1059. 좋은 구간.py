import sys
input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
N = int(input())
S.sort()
left = 0
right = 0

for idx in range(L):
    if S[idx] == N:
        print(0)
        break
    elif S[idx] > N:
        left = 1
        right = S[idx]-1
        print((N-left)*(right-N+1)+(right-N))
        break
    elif S[idx] < N and S[idx+1] > N:
        left += S[idx]+1
        right += S[idx+1]-1
        print((N-left)*(right-N+1)+(right-N))
        break
    else:
        continue

    