import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1):
    x, y, w, h = map(int, input().split())
    mn = 1e9
    lst = [x, y, w-x, h-y]
    for i in range(4):
        if mn > lst[i]:
            mn = lst[i]
    print(mn)