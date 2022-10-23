import sys
input = sys.stdin.readline
cnt_lst = [0] * 10001
for _ in range(int(input())):
    cnt_lst[int(input())] += 1
for idx in range(1, 10001):
    if cnt_lst[idx] > 0:
        for i in range(cnt_lst[idx]):
            print(idx)
