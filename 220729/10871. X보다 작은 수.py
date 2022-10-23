import sys

# N이 갯수, X가 특정 정수
N, X = map(int, sys.stdin.readline().split())

sequence = list(map(int, sys.stdin.readline().split()))[:N]

answer = ''
for i in sequence:
    if int(i) < X:
        answer += str(i) + ' '

print(answer)

