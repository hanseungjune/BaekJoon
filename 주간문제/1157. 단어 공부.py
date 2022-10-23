word = list(input().upper())
set_word = set(word)
dict_word = {}

for i in set_word:
    dict_word[i] = word.count(i)
# print(dict_word) #{'I': 4, 'S': 4, 'P': 1, 'M': 1}

all_values = list(dict_word.values())
max_value = max(all_values)

if all_values.count(max_value) > 1:
    print('?')
else:
    for key, value in dict_word.items():
        if max_value == dict_word[key]:
            print(key)
