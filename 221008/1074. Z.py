import sys;sys.stdin=open('input.txt','r')

def zET(n, y, x):
    global cnt, r, c
    # 찾으면 바로 출력하고 끝내기
    if y == r and x == c:
        print(int(cnt))
        exit(0)

    # 재귀를 최대로 했을때, n == 1이면 +1씩 더하면서 구하는 거 가능
    if n == 1:
        cnt += 1
        return

    # 정해진 z범위 찾기(n이 1이라고 가정하고 봐야 범위 도출 가능)
    if not (y <= r < y+n and x <= c < x+n):
        cnt += n**2
        return

    # n/2가 1이 될때까지 재귀
    zET(n/2, y, x)
    zET(n/2, y, x+n/2)
    zET(n/2, y+n/2, x)
    zET(n/2, y+n/2, x+n/2)

N, r, c = map(int, input().split())
cnt = 0

zET(2**N, 0, 0)