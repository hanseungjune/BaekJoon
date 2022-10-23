alpha = [chr(i) for i in range(65, 91)]

alpha_lst = [alpha[:3], alpha[3:6], alpha[6:9], alpha[9:12], alpha[12:15], alpha[15:19], alpha[19:22], alpha[22:26]]
alpha_sec = [i for i in range(3, 11)]

lst = []
for up in input():
    lst += [alpha_sec[i] for i in range(8) if up in alpha_lst[i]]
print(sum(lst))





