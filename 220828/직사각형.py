import sys
sys.stdin = open('input.txt','r')

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # (d)인 경우 부터
    if p2 < x1 or p1 < x2 or q1 < y2 or y1 > q2:
        print('d')
    # (c)인경우 구분하고, 첫번째 조건은 만족하나, 2번째 조건 만족안하면 선분이 겹치는거라고 볼수 있어서, (b)가 될 수 있음
    # 세로로 이동함
    elif x1 == p2:
        if q1 == y2 or y1 == q2:
            print('c')
        else:
            print('b')
    elif p1 == x2:
        if q1 == y2 or q2 == y1:
            print('c')
        else:
            print('b')
    # 가로로 이동함
    elif q1 == y2:
        if x1 == p2 or x2 == p1:
            print('c')
        else:
            print('b')
    elif y1 == q2:
        if x1 == p2 or x2 == p1:
            print('c')
        else:
            print('b')
    else:
        print('a')
