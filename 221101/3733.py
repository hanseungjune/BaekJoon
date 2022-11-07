import sys; sys.stdin = open('input.txt','r')

result = []

while True:
    try:
        n, s = map(int, input().split())
        result.append(s//(n+1))
    except:
        for r in result:
            print(r)
        break
