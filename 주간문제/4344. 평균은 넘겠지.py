T = int(input())

for i in range(T):
    N, *rest = list(map(int, input().split()))

    avg = sum(rest)/N
    cnt = 0
    for ele in rest:
        if ele > avg:
            cnt += 1
    print(f'{(cnt/N)*100:.3f}%')


