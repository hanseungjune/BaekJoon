N = int(input())

hansu = 0
if N < 100:
    hansu += N
else: # N > 100
    hansu = 99
    for str_ in range(100, N+1):
        chars = list(str(str_))
        diff_1 = int(chars[0]) - int(chars[1])
        diff_2 = int(chars[1]) - int(chars[2])
        if diff_1 == diff_2:
            hansu += 1
        else:
            continue
print(hansu)
