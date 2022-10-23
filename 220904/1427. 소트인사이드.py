lst = list(map(int, input()))
lst.sort(reverse=True)
answer = ''.join(map(str, lst))
print(answer)