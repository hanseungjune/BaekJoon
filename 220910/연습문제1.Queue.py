queue = []
for i in range(1, 4):
    queue.append(i)

for j in range(1, 4):
    a = queue.pop(0)
    print(a, end=' ')
