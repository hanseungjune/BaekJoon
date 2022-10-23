import datetime
import sys
input = sys.stdin.readline
y1,m1,d1 = map(int,input().split())
y2,m2,d2 = map(int,input().split())

D = int(str(datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).split()[0])
# 26나옴

full = 0 #full 365243일보다 더 지나면 gg
for i in range(1000) :
    if i%400==0 :
        full += 366
    elif i%100==0 :
        full += 365
    elif i%4==0 :
        full += 366
    else :
        full += 365
# print(full)
if D >= full :
    print('gg')
else :
    print(f'D-{D}')

