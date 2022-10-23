import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')
N = int(input())
lst = [int(input()) for i in range(N)]
lst.sort()
# 최빈도
lst_s = Counter(lst).most_common()
# print(lst_s)
print(round(sum(lst)/N))
print(lst[N//2])
if len(lst_s) > 1:
    if lst_s[0][1] == lst_s[1][1]:
        print(lst_s[1][0])
    else:
        print(lst_s[0][0])
else:
    print(lst_s[0][0])
print(lst[-1]-lst[0])

