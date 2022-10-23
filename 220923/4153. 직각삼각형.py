import sys; sys.stdin = open('input.txt', 'r')

while True:
    ans = 0
    a, b, c = map(int, input().split())


    if a == 0 and b == 0 and c == 0:
        break

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
        ans = 1

    if ans:
        print('right')
    else:
        print('wrong')