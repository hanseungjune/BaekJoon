A = int(input())
B = int(input())
C = int(input())

multi = list(str(A*B*C))

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(multi)  # ['1', '7', '0', '3', '7', '3', '0', '0']

for i in lst:
    if i in multi:
        print(multi.count(i))