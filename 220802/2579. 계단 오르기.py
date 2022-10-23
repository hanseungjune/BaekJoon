import sys
input = sys.stdin.readline
T = int(input())
lst = [0]*(T+1)
dp = [0]*(T+1)
for _ in range(1, T+1):
    lst[_] = int(input())
if T >= 1:
    dp[1] = lst[1]
    
if T >= 2:
    dp[2] = lst[1] + lst[2]

if T >= 3:
    dp[3] = max(lst[1] + lst[3], lst[2] + lst[3])

for idx in range(4, T+1):
    dp[idx] = max(dp[idx-2] + lst[idx], dp[idx-3] + lst[idx-1] + lst[idx])

print(dp[T])