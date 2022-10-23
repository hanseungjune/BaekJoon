# def tiling(n):
#     if n == 1 or n == 0:
#         return 1
#     else: # n > 1
#         return tiling(n-1) + tiling(n-2)*2
import sys
input = sys.stdin.readline

n = int(input())
tile_lst = [1, 1]
for i in range(2, n+1):
    tile_lst.append(tile_lst[i-2]*2 + tile_lst[i-1])
print(tile_lst[-1]%10007)

