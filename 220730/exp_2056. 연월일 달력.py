last_31th = [1, 3, 5, 7, 8, 10, 12]
last_30th = [4, 6, 9, 11]
last_28th = [2]
months = [x for x in range(1, 13)]

T = int(input())
for t in range(1, T+1):
    date_input = input()
    year = date_input[:4]
    mon = date_input[4:6]
    day = date_input[6:]

    for month in months:
        if int(mon) in months:
            if int(mon) in last_31th:
                if int(day) > 0 and int(day) <= 31:
                    print(f'#{t} {year}/{mon}/{day}')
                else:
                    print(f'#{t} -1')
            elif int(mon) in last_30th:
                if int(day) > 0 and int(day) <= 30:
                    print(f'#{t} {year}/{mon}/{day}')
                else:
                    print(f'#{t} -1')
            else:   # 28일
                if int(day) > 0 and int(day) <= 28:
                    print(f'#{t} {year}/{mon}/{day}')
                else:
                    print(f'#{t} -1')
            break
        else:
            print(f'#{t} -1')
            break

# dict
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# a = dict()
# for idx, day in enumerate(days, start=1):
#     a[idx] = day
#
# print(a)