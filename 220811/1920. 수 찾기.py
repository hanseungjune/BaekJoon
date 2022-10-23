import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dict = {}
for key in A:
    dict[key] = 1
# print(dict)

M = int(input())
B = list(map(int, input().split()))
for val in B:
    try:
        print(dict[val])
    except KeyError:
        print(0)