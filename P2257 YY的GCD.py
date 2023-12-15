N = 10000001

is_prime = [True] * N
primes = []

mu = [0] * N
mu[1] = 1

f = [0] * N

for i in range(2, N):
    if is_prime[i]:
        primes.append(i)
        mu[i] = -1
        f[i] = 1
    for p in primes:
        t = i * p
        if t >= N:
            break
        is_prime[t] = False
        if i % p == 0:
            mu[t] = 0
            f[t] = mu[i]
            break
        mu[t] = -mu[i]
        f[t] = mu[i] - f[i]
    f[i] += f[i - 1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n

    ans = 0
    l = 1
    while l <= n:
        tn, tm = n // l, m // l
        r = min(n // tn, m // tm)
        ans += (f[r] - f[l - 1]) * tn * tm
        l = r + 1
    print(ans)
