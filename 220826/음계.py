result = list(map(int, input().split()))

ascending = sorted(result)
descending = sorted(result, reverse=True)

if result == ascending:
    print('ascending')
elif result == descending:
    print('descending')
else:
    print('mixed')