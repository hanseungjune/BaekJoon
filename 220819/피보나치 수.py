def fibo(a):
    if a <= 1:
        return a
    return fibo(a-1) + fibo(a-2)

print(fibo(int(input())))