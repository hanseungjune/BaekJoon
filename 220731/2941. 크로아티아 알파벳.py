cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in cro_alpha:
    if i in word:
        word = word.replace(i, 'a')

print(len(word))
