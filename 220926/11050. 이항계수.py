import sys; sys.stdin = open('input.txt','r')


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

N, K = map(int, input().split())
top = factorial(N)
bottom = factorial(N-K)*factorial(K)
answer = top//bottom
print(answer)
