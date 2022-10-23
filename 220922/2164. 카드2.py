from collections import deque

N = int(input())
lst = deque(_ for _ in range(1, N+1))

while len(lst) > 1:
    delete_ele = lst.popleft()
    plus = lst.popleft()
    lst.append(plus)

print(''.join(map(str, lst)))