import sys
input = sys.stdin.readline

num = int(input())

lst = []
if num != 1:
    for i in range(2, num+1):
        if num % i == 0:
            lst.append(i)
    result_lst = []
    for j in lst:
        while True:
            if num % j == 0:
                result_lst.append(j)
                num = num // j
            else:
                break
        if num == 1:
            break

    for _ in result_lst:
        print(_)