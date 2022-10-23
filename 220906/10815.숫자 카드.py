import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')