import sys
sys.stdin = open('빙고.txt', 'r')
input = sys.stdin.readline

check = [0]*12      # 0~4 col / 5~9 row / 10 오르쪽하단 대각 / 11 왼쪽하단 대각
# 적어둔거
lst = [list(map(int, input().split())) for _ in range(5)]
flag = False

def sum_check(lst):
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += lst[j][i]
        check[i] = sum
        kum = 0
        for k in range(5):
            kum += lst[i][k]
        check[i+5] = kum

        r_d = 0
        for a in range(5):
            r_d += lst[a][a]
        check[10] = r_d
        l_d = 0
        for b in range(5):
            l_d += lst[b][4 - b]
        check[11] = l_d
    return check

# print(sum_check(lst)) # [74, 52, 35, 85, 79, 59, 58, 69, 54, 85, 49, 44]

# 부르는거
arr = list(map(int, input().split()))
for _ in range(4):
    arr += list(map(int, input().split()))

cnt = 0
for n in range(25):
    remove = arr[n]
    for i in range(5):
        for j in range(5):
            if lst[i][j] == remove:
                lst[i][j] = 0
                sum_check(lst)
                cnt += 1
                if check.count(0) >= 3:
                    flag = True
                    break
        if flag == True:
            break
    if flag == True:
        print(cnt)
        break

