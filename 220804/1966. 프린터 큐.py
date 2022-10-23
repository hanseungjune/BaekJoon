import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, wd = map(int, input().split())

    deque = list(map(int, input().split()))

    cnt = 0
    while True:
        if deque[0] < max(deque):
            a = deque.pop(0)
            wd -= 1
            if wd == -1:
                wd = len(deque)
            deque.append(a)
        else: #deque[0] >= max(deque)  
            if wd == 0:
                cnt += 1
                print(cnt)
                break
            wd -= 1
            del deque[0]
            cnt += 1