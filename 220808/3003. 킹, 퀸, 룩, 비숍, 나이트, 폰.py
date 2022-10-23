chessboard = [1, 1, 2, 2, 2, 8]
lst = input().split()
output = ""

for i in range(len(lst)):
    output += str(chessboard[i]-int(lst[i]))+" "

print(output)
