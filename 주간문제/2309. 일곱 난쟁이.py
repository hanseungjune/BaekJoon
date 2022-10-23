import itertools

hobbit_nine = [int(input()) for _ in range(9)]

seven_combis = list(itertools.combinations(hobbit_nine, 7))
for seven_combi in seven_combis:
    if sum(seven_combi) == 100:
        for height in sorted(seven_combi):
            print(height)
        break