def push_front(x):
    return deq.insert(0, x)

def push_back(x):
    return deq.append(x)

def pop_front(deq):
    if deq == []:
        return -1
    else:
        return deq.pop(0)

def pop_back(deq):
    if deq == []:
        return -1
    else:
        return deq.pop(-1)

def size(deq):
    return len(deq)

def empty(deq):
    if deq == []:
        return 1
    else:
        return 0

def front(deq):
    if deq == []:
        return -1
    else:
        return deq[0]

def back(deq):
    if deq == []:
        return -1
    else:
        return deq[-1]

import sys
input = sys.stdin.readline
deq = []

T = int(input())

for _ in range(T):
    order = list(map(str, input().rstrip().split()))
    if order[0] == 'push_front':
        push_front(order[1])
    elif order[0] == 'push_back':
        push_back(order[1])
    elif order[0] == 'pop_front':
        print(pop_front(deq))
    elif order[0] == 'pop_back':
        print(pop_back(deq))
    elif order[0] == 'size':
        print(size(deq))
    elif order[0] == 'empty':
        print(empty(deq))
    elif order[0] == 'front':
        print(front(deq))
    elif order[0] == 'back':
        print(back(deq))








