import sys
sys.stdin = open('input.txt','r')


while True:
    word = input()
    palindrome = word[::-1]
    if word == '0':
        break
    else:
        if word == palindrome:
            print('yes')
        else:
            print('no')