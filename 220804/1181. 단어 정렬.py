import sys
input = sys.stdin.readline

N = int(input())
lst = [input().rstrip() for _ in range(N)]
real_lst = sorted(list(set(lst)))
real_lst.sort(key=lambda x : len(x))

for aaa in range(len(real_lst)):
    print(real_lst[int(aaa)])