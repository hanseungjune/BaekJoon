N = int(input())

Q1,Q2,Q3,Q4,AXIS = 0,0,0,0,0

for tc in range(1, N+1):
    x, y = map(int, input().strip().split())

    if x == 0:
        AXIS += 1
    elif y == 0:
        AXIS += 1
    elif x > 0:
        if y > 0:
            Q1 += 1
        elif y < 0:
            Q4 += 1
    elif x < 0:
        if y > 0:
            Q2 += 1
        elif y < 0:
            Q3 += 1

print(f'Q1: {Q1} ')
print(f'Q2: {Q2} ')
print(f'Q3: {Q3} ')
print(f'Q4: {Q4} ')
print(f'AXIS: {AXIS}')