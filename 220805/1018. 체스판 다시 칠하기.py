import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))

lst = []
cnt_lst = []

for _ in range(N):
    lst.append(list(input().split('\n')[0]))

for big_row in range(N-7):
    for big_col in range(M-7):
        w_idx, b_idx = 0, 0
        for sm_row in range(big_row, big_row+8):
            for sm_col in range(big_col, big_col+8):
                if (sm_row+sm_col)%2 == 0:
                    if lst[sm_row][sm_col] != 'W':
                        w_idx += 1
                    if lst[sm_row][sm_col] != 'B':
                        b_idx += 1
                else:
                    if lst[sm_row][sm_col] != 'W':
                        b_idx += 1
                    if lst[sm_row][sm_col] != 'B':
                        w_idx += 1
        cnt_lst.append(b_idx)
        cnt_lst.append(w_idx)
print(min(cnt_lst))