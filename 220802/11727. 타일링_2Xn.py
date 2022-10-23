import sys
input = sys.stdin.readline

N = int(input())

dp = [1, 1]

for idx in range(2, N+1):
    dp.append(dp[idx-1]+2*dp[idx-2])

print(dp[-1]%10007)