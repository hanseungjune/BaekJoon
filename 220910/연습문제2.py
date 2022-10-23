def backtrack(a,k,sum):
    c = [True, False]

    #마지막 노드까지 도착한 경우 합이 10인 경우만 출력하자!
    if k == 10:
        if sum == 10:
            for i in range(1, 11):
                if a[i] == 1:
                    print(i, end=' ')
            print()
    else:
        k+=1
        if sum + k <= 10:
            #합이 10이하 일때만 본인을 선택한다.
            a[k] = 1
            backtrack(a, k, sum+k)
        a[k] = 0; backtrack(a,k,sum)

a = [0] * 11
k = 0
backtrack(a, k, 0)