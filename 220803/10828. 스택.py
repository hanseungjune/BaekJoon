def push(x):
    return stack.append(x)
def pop(stack):
    if stack == []:
        return -1
    else:
        return stack.pop()
def size(stack):
    return len(stack)
def empty(stack):
    if stack == []:
        return 1
    else:
        return 0
def top(stack):
    if stack == []:
        return -1
    else:
        return stack[-1]

stack = []

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    order = list(map(str, input().rstrip().split()))
    if order[0] == 'push':
        push(int(order[1]))
    elif order[0] == 'pop':
        print(pop(stack))
    elif order[0] == 'size':
        print(size(stack))
    elif order[0] == 'empty':
        print(empty(stack))
    elif order[0] == 'top':
        print(top(stack))