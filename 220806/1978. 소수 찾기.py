import sys
input = sys.stdin.readline

T = int(input())

answer = list(map(int, input().split()))
# lst = []

# for num in answer:
#     yaksu_lst = []
#     for idx in range(1, num+1):
#         if num % idx == 0:
#             yaksu_lst.append(idx)
#     lst.append(yaksu_lst)

# cnt = 0

# for _ in range(len(lst)):
#     if len(lst[_]) != 2:
#         continue
#     else:
#         cnt += 1

# print(cnt)

cnt = 0
for n in answer:
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            cnt += 1
print(cnt)