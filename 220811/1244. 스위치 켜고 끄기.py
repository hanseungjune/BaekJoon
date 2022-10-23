import sys
sys.stdin = open('input.txt', 'r')

switch_cnt = int(input())
switch = list(map(int, input().split()))
T = int(input())

for tc in range(1, T+1):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number, switch_cnt+1, number):
            if switch[i-1]:
                switch[i-1] = 0
            elif switch[i-1] == 0:
                switch[i-1] = 1

    elif gender == 2:
        if switch[number-1] == 0:
            switch[number-1] = 1
        else:
            switch[number-1] = 0
        for i in range(1, 50):
            if (0 <= number-i-1 and number+i-1 < switch_cnt) and (switch[number-i-1] == switch[number+i-1]):
                if switch[number-i-1] == 0:
                    switch[number-i-1] = 1
                    switch[number+i-1] = 1
                else:
                    switch[number-i-1] = 0
                    switch[number+i-1] = 0
            elif (0 <= number-i-1 and number+i-1 < switch_cnt) and switch[number-i-1] != switch[number+i-1]:
                break

count = 0
while count < len(switch):
    if count % 20 == 19:
        print(switch[count], end='')
        print()
    elif count+1 == switch_cnt:
        print(switch[count], end='')
    else:
        print(switch[count], end=' ')
    count += 1