import sys; sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

N = int(input())
lsts = sorted(list(map(int, input().split())))
M = int(input())
arrs = list(map(int, input().split()))

lst_dict = {}
for lst in lsts:
    if lst in lst_dict:
        lst_dict[lst] += 1
    else:
        lst_dict[lst] = 1

def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return lst_dict.get(target)
    if arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    if arr[mid] > target:
        return binarySearch(arr, target, start, mid-1)

for target in arrs:
    print(binarySearch(lsts, target, 0, len(lsts)-1), end=' ')
