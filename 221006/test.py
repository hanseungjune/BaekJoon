import itertools

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]

def solution(orders, course):

    res = []
    for cour in course:
        order_set = set()
        for order in orders:
            for elem in order:
                order_set.add(elem)
        order_menu = sorted(list(order_set))

        order_combi = itertools.combinations(order_menu, cour)
        order_combinations = list(order_combi)

        n_dict = {}
        for order in order_combinations:
            temp = ''.join(order)
            n_dict[temp] = 0

        for order in orders:
            order_combi2 = itertools.combinations(order, cour)
            order_combinations2 = list(order_combi2)
            for combi in order_combinations2:
                temp = ''.join(sorted(combi))
                n_dict[temp] += 1

        mx = 0
        for value in n_dict.values():
            if mx < value:
                mx = value

        for key in n_dict.keys():
            if n_dict[key] == mx and mx >= 2:
                res.append(key)

    res.sort()
    return res

print(solution(orders, course))
