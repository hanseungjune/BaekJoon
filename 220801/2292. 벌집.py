N = int(input())

start = 1
floor = 1

if N == 1:
    print(1)
else:
    while True:
        if start < N:
            start += 6*floor
            floor += 1
        else:
            print(floor)
            break