import sys;sys.stdin = open('input.txt','r')
# R은 뒤집기(배열의 순서를 리버스)
# D는 버리기(첫번째 수를 버림 인덱스 0)

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    direction = True
    try:
        nums = input().lstrip("[").rstrip("]\n")
        if nums == "":
            nums = []
        else:
            nums = deque(list(map(int, nums.split(","))))
        for x in p:
            if x=="R":
                direction = not direction
            elif x=="D":
                if direction:
                    nums.popleft()
                else:
                    nums.pop()
        if not direction:
            nums = list(nums)[::-1]
        print("[", end="")
        print(",".join(map(str,nums)), end="")
        print("]")
    except:
        print("error")
