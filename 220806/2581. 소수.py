import sys
input = sys.stdin.readline

n_num = int(input())
x_num = int(input())
lst = []

for num in range(n_num, x_num+1):
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            lst.append(num)

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])