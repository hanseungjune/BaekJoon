import sys
sys.stdin = open('input.txt','r')

N = int(input())

i = 665
cnt = 0
while True:
    i += 1
    if '666' in str(i):
        cnt += 1
        if cnt == N:
            print(i)
            break
