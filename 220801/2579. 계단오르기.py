import sys
input = sys.stdin.readline

T = int(input())
dp = [0 for _ in range(T+2)]
stair = [0 for _ in range(T+2)]
for k in range(1, T+1):
    stair[k] += int(input())

dp[1] = stair[1]
dp[2] = dp[1] + stair[2]
dp[3] = max(dp[1] + stair[3], stair[2] + stair[3])

for i in range(4, T+1):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
print(dp[T])

