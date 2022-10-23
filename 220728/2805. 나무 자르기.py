import sys

tree_cnt, target = map(int, sys.stdin.readline().split())
tree_lst = list(map(int, sys.stdin.readline().split()))
tree_lst.sort()

left = 0
right = max(tree_lst)
result = 0

while left <= right:
    mid = (left+right)//2
    sum = 0
    for tree in tree_lst:
        if tree > mid:
            sum += tree-mid
            if sum >= target:
                break
    if sum >= target:
        result = mid
        left = mid+1
    else:
        right = mid-1
print(result)
