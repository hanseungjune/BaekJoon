import sys; sys.stdin=open('input.txt', 'r')

N = int(input())
lst = input()
i = 0
sm = 0
for l in lst:
    ans = ord(l)-96
    sm += ans*(31**i)
    i += 1

print(sm)