import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt','r')

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for tc in range(T):
    N = int(input())

    a, b = N//2, N//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1