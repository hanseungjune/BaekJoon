N = int(input())

if N < 10:
    N1 = N
    cnt = 0
    while True:
        sum = N//10 + N%10
        if sum < 10:
            N = (N%10)*10 + sum
        else: #sum >= 10:
            sum = sum%10
            N = (N%10)*10 + sum
        cnt += 1
        if N1 == N:
            break
        else:
            continue
else:
    N1 = N
    cnt = 0
    while True:
        sum = N//10 + N%10
        if sum < 10:
            N = (N%10)*10 + sum
        else: #sum >= 10:
            sum = sum%10
            N = (N%10)*10 + sum
        cnt += 1
        if N1 == N:
            break
        else:
            continue
print(cnt)
