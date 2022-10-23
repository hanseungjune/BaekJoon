num = int(input())
sums = 0
floor = 0

while num > sums:
    floor += 1
    sums += floor

gap = sums - num
if floor % 2 == 1:
    top = sums - num + 1
    bottom = floor - gap
else: #floor % 2 == 0:
    top = floor - gap
    bottom = gap + 1

print(f'{top}/{bottom}')