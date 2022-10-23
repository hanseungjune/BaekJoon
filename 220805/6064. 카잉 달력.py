import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, a, b = map(int, input().split())
    i = 0
    j = 0
    while True:
        red = M*i+a
        blue = N*j+b
        if red > (M*N) or blue > (M*N):
            print(-1)
            break
        elif red < blue:
            i += 1
        elif red > blue:
            j += 1
        elif red == blue:
            print(red)
            break
        



        