import sys
sys.stdin = open('input.txt', 'r')

lst = list(map(int, input().split()))
pow = 0
for i in lst:
    pow += i**2
pow %= 10
print(pow)