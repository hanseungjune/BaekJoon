import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst_rev = [(y, x) for (x, y) in lst]
ans = sorted(lst_rev)
result = [(y, x) for (x, y) in ans]

for res in result:
    print(f'{res[0]} {res[1]}')