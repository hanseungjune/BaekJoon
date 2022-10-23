import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

max_val = max(lst)
sum_lst = []
for i in lst:
    sum_lst.append(int(i)/max_val*100)
print(sum(sum_lst)/N)