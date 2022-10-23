T = int(input())

for _ in range(T):
    N, word = map(str, input().split())
    answer = ''.join([i*int(N) for i in word])
    print(answer)