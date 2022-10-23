def gcd(a, b):
    global ans
    if b == 0:
        ans = a
        return
    gcd(b, a % b)

def lcm(a, b):
    global ans, res
    res = (a * b)//ans
    return

a, b = map(int, input().split())
ans = 0
res = 0
gcd(a, b)
lcm(a, b)

print(ans)
print(res)