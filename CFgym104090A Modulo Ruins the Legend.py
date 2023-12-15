def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    y, x, gcd = exgcd(b, r)
    return x, y - q * x, gcd


n, m = map(int, input().split())

su = sum(map(int, input().split())) % m

s, d, t = exgcd(n, (n * (n + 1)) >> 1)
x, y, g = exgcd(t, m)
k = (m - su + g - 1) // g
x *= k
print((su + k * g) % m)
print(s * x % m, d * x % m)
