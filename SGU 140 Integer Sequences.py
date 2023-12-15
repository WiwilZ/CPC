def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, gcd = exgcd(b, r)
    return y, x - q * y, gcd


n, p, b = map(int, input().split())
A = list(map(int, input().split()))
A.append()
gcd = 0
for i, a in enumerate(map(int, input().split())):
    x, y, gcd = exgcd(gcd, a)
    X = [e * x % p for e in X] + [y]

x, y, gcd = exgcd(gcd, p)
q, r = divmod(b, gcd)
if r != 0:
    print('NO')
else:
    print('YES')
    for e in X:
        print(e * x % p * q % p, end=' ')

