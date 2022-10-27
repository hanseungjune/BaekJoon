def solve(x, y):
    return (x+y)*(x-y)

x, y = map(int, input().split())
print(solve(x, y))