N = 1000001

is_prime = [True] * N
primes = []

f = [0] * N
f[1] = 1

for i in range(2, N):
    if is_prime[i]:
        primes.append(i)
        f[i] = 1 + i * (i - 1)
    for p in primes:
        t = i * p
        if t >= N:
            break
        is_prime[t] = False
        if i % p == 0:
            f[t] = f[i] + (f[i] - f[i // p]) * p * p
            break
        f[t] = f[i] * f[p]

for _ in range(int(input())):
    n = int(input())
    print((n * (f[n] + 1)) >> 1)
