alphabets = [chr(i) for i in range(97,123)]

put = input()
answer = ""
for alpha in alphabets:
    answer += str(put.find(alpha)) + ' '

print(answer)
