import sys
sys.stdin = open('input.txt','r')

chamwoi = int(input())

# 1과 2의 길이, 3과 4의 길이가 같으면 탈출!

total = []
for _ in range(6):
    direction, meter = map(int, input().split())
    total.append((direction, meter))
    #세가세가세가

    mx_height, mx_width = 0, 0
    for direc, met in total:
        # 위아래
        if direc == 4 or direc == 3:
            if mx_height < met:
                mx_height = met
        elif direc == 2 or direc == 1:
            if mx_width < met:
                mx_width = met

max_area = mx_width * mx_height

mx_wid_idx = 0
mx_hei_idx = 0
# 최대값 인덱스(가로 세로)
for i in range(6):
    if total[i][1] == mx_width:
        mx_wid_idx = i
    if total[i][1] == mx_height:
        mx_hei_idx = i

# 너비로 작은 높이 구하고, 높이고 작은 너비 구함
small_height = abs(total[mx_wid_idx+5 if mx_wid_idx == 0 else mx_wid_idx-1][1] - total[(mx_wid_idx+1)%6][1])
small_width = abs(total[mx_hei_idx+5 if mx_hei_idx == 0 else mx_hei_idx-1][1] - total[(mx_hei_idx+1)%6][1])

min_area = small_width*small_height

answer = (max_area - min_area) * chamwoi
print(answer)
#
# print(mx_wid_idx, mx_hei_idx)
# print(total)








