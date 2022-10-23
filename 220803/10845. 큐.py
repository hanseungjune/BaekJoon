def push(x):
<<<<<<< HEAD
    return que.append(x)

def pop(que):
    if que == []:
        return -1
    else:
        return que.pop(0)

def size(que):
    return len(que)

def empty(que):
    if que == []:
=======
    return queue.append(x)

def pop(queue):
    if queue == []:
        return -1
    else:
        return queue.pop(0)

def size(queue):
    return len(queue)

def empty(queue):
    if queue == []:
>>>>>>> f95cc7fc64b4e01781432a973434194f778c9181
        return 1
    else:
        return 0

<<<<<<< HEAD
def front(que):
    if que == []:
        return -1
    else:
        return que[0]

def back(que):
    if que == []:
        return -1
    else:
        return que[-1]

que = []
=======
def front(queue):
    if queue == []:
        return -1
    else:
        return queue[0]

def back(queue):
    if queue == []:
        return -1
    else:
        return queue[-1]

queue = []
>>>>>>> f95cc7fc64b4e01781432a973434194f778c9181

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    order = list(map(str, input().rstrip().split()))
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
<<<<<<< HEAD
        print(pop(que))
    elif order[0] == 'size':
        print(size(que))
    elif order[0] == 'empty':
        print(empty(que))
    elif order[0] == 'front':
        print(front(que))
    elif order[0] == 'back':
        print(back(que))
=======
        print(pop(queue))
    elif order[0] == 'size':
        print(size(queue))
    elif order[0] == 'empty':
        print(empty(queue))
    elif order[0] == 'front':
        print(front(queue))
    elif order[0] == 'back':
        print(back(queue))
>>>>>>> f95cc7fc64b4e01781432a973434194f778c9181



