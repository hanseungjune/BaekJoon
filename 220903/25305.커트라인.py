import sys
sys.stdin = open('input.txt', 'r')

N, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
print(lst[k-1])