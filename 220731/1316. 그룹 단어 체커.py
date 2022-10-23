import sys
input = sys.stdin.readline

T = int(input())
answer = 0

for _ in range(T):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            break
    else:
        answer+=1
print(answer)

