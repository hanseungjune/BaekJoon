import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    queue = deque()
    queue.append((A, ''))
    visited = [0]*10000

    while queue:
        num, dslr = queue.popleft()
        visited[num] = 1
        if num == B:
            print(dslr)
            break

        #D
        number = (2*num)%10000
        if not visited[number]:
            queue.append((number, dslr+'D'))
            visited[number] = 1

        #S
        number = (num-1)%10000
        if not visited[number]:
            queue.append((number, dslr + 'S'))
            visited[number] = 1

        #L
        number = ((num%1000)*10+(num//1000))%10000
        if not visited[number]:
            queue.append((number, dslr + 'L'))
            visited[number] = 1

        #R
        number = (num//10+(num%10)*1000)%10000
        if not visited[number]:
            queue.append((number, dslr + 'R'))
            visited[number] = 1