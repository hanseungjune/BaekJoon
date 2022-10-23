import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for number in range(M, N+1):
    for divi in range(2, int(number**0.5)+1):
        if number % divi == 0:
            break
    else:
        if number != 1:
            print(number)
