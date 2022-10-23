import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        if n == 0:
            break
        cnt = 0
        for number in range(n+1, 2*n+1):
            for i in range(2, int(number**0.5)+1):
                # 나머지가 나오는 순간 약수가 있음으로 소수가 아님
                if number % i == 0:
                    break
            # 다 그냥 돌았다면 약수는 없다는 뜻임
            else:
                cnt += 1
        print(cnt)
    except:
        break