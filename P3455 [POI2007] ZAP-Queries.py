N = 50001

is_prime = [True] * N
primes = []

mu = [0] * N
mu[1] = 1

for i in range(2, N):
    if is_prime[i]:
        primes.append(i)
        mu[i] = -1
    for p in primes:
        t = i * p
        if t >= N:
            break
        is_prime[t] = False
        if i % p == 0:
            mu[t] = 0
            break
        mu[t] = -mu[i]
    mu[i] += mu[i - 1]

for _ in range(int(input())):
    a, b, d = map(int, input().split())
    if a > b:
        a, b = b, a
    a //= d
    b //= d
    ans = 0
    l = 1
    while l <= a:
        ta, tb = a // l, b // l
        r = min(a // ta, b // tb)
        ans += (mu[r] - mu[l - 1]) * ta * tb
        l = r + 1
    print(ans)
