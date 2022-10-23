i = 0
lst = []
while i < 10:
    N = int(input())
    rest = N%42
    lst.append(rest)
    i += 1

print(len(set(lst)))
