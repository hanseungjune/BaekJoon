import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [int(input()) for x in range(N)]
lst.sort()

for i in lst:
    print(i)
