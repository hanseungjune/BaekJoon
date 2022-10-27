T = int(input())

for tc in range(1, T+1):
    str1 = input()
    ans = ''
    ans += str1[0]
    ans += str1[-1]
    print(ans)