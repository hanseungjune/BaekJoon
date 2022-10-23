T = int(input())

for i in range(T):
    ox = list(input())
    score = 0
    cnt = 0
    for ele in ox:
        if 'O' == ele:
            cnt += 1
            score += cnt
        else: 
            cnt = 0
    print(score)