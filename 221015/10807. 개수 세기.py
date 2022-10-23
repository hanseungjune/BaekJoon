N = int(input())
lst = list(map(int, input().split()))
target = int(input())

cnt = 0
for res in lst:
    if res == target:
        cnt += 1

print(cnt)