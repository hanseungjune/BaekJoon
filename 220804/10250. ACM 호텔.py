import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    lst = []
    
    H, W, N = map(int, input().split())
    
    for w in range(1, W+1):
        for h in range(1, H+1):
            if int(w) < 10:
                lst.append(str(h)+f'0{w}')
            else:
                lst.append(str(h)+str(w))
    print(lst[N-1])