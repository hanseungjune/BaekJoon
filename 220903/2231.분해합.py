import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

problem = int(input())
# 1부터 1000000까지
N_lst = [str(x) for x in range(1, problem)]
flag = False

lst = []
original = 0
for N in N_lst:
    original = int(N)
    for n in N:
        original += int(n)
    if original == problem:
        print(N)
        break
else:
    print(0)
