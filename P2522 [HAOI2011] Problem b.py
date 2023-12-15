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
    a, b, c, d, k = map(int, input().split())
    if b > d:
        a, b, c, d = c, d, a, b
    a, b, c, d = (a - 1) // k, b // k, (c - 1) // k, d // k
    ans = 0
    l = 1
    while l <= b:
        ta, tb, tc, td = a // l, b // l, c // l, d // l
        r = min(b // tb, d // td)
        if ta:
            r = min(r, a // ta)
        if tc:
            r = min(r, c // tc)
        ans += (mu[r] - mu[l - 1]) * (tb - ta) * (td - tc)
        l = r + 1
    print(ans)

