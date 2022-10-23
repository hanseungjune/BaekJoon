# def gener(end, start=1):
#     if start > end:
#         return []
#     total = start
#     for i in str(start):
#         total += int(i)
#
#     start += 1
#     return [total] + gener(end, start)
#
# def find_self_number(end):
#     number_set = set([i for i in range(1, end+1)])
#     not_self_number_set = set(gener(end))
#     self_number_set = sorted(list(number_set - not_self_number_set))
#     return self_number_set
#
# for self_number in find_self_number(996):
#     print(self_number)

def gener(num):
    num_lst = str(num)
    for i in num_lst:
        num += int(i)
    return num

number_set = set([x for x in range(1, 10000)])
not_self_nums_set = set([gener(j) for j in range(1, 10000)])
self_nums_lst = sorted(list((number_set)-(not_self_nums_set)))

for self_num in self_nums_lst:
    print(self_num)

