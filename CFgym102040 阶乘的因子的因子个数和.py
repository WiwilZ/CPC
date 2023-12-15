N = 1000001

is_prime = [True] * N
primes = []

for i in range(2, N):
    if is_prime[i]:
        primes.append(i)
    for p in primes:
        t = i * p
        if t >= N:
            break
        is_prime[t] = False
        if i % p == 0:
            break

mod = 10000007
while n := int(input()):
    ans = 1
    for p in primes:
        if p > n:
            break
        cnt = 0
        m = n
        while m:
            m //= p
            cnt += m
        ans = (ans * (((cnt + 1) * (cnt + 2)) >> 1)) % mod
    print(ans)
