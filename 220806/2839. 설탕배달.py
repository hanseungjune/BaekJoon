import sys
input = sys.stdin.readline

sugar = int(input())

three_cnt = sugar//3
five_cnt = sugar//5

lst = []

for i in range(three_cnt+1):
    for j in range(five_cnt+1):
        if 3*i + 5*j == sugar:
            lst.append(i+j)
        else:
            continue

if not lst:
    print(-1)
else:
    print(min(lst))