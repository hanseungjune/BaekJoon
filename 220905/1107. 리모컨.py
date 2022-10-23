# 현재 채널은 100번
# 0번에서 '-' 누르면 0임

import sys
sys.stdin = open('input.txt', 'r')

target = int(input())
M = int(input())
if M > 0:
    broken_btn = list(map(int, input().split()))
else:
    broken_btn = list()
# 100번에서 +, - 눌러서 가는 횟수
# 누를수 있는 버튼을 이용하여 누르고 가능한 버튼을 누른것과 원하는 채널간의 차이를 구해서 횟수 구하기

# 100번에 누르면?
answer = abs(100-target)
# 누를수 있는 버튼을 이용하여 누르고 가능한 버튼을 누른것과 원하는 채널간의 차이를 구해서 횟수 구하기
for number in range(1000001):
    for num in str(number):
        if int(num) in broken_btn:
        # 리모컨 누르다가 안눌리면 빨리 채널버튼으로 눌러야지!(그래서 break)
            break
    else:   #번호를 눌러서 만들수 있는 경우
        answer = min(answer, len(str(number))+abs(target-number))
print(answer)








