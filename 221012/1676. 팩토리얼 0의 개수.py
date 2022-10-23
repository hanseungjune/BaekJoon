import sys;sys.stdin=open('input.txt','r')

N = int(input())
cnt = 0

while N >= 5:
    cnt += N//5
    N //= 5

print(cnt)