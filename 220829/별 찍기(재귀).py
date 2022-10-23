def star_arr(N):
    if N == 1:
        return ['*']

    star = star_arr(N//3)
    lst = []

    for s in star:
        lst.append(s * 3)
    for s in star:
        lst.append(s+' '*(N//3)+s)
    for s in star:
        lst.append(s * 3)

    return lst

N = int(input())
for row in star_arr(N):
    print(''.join(map(str, row)))