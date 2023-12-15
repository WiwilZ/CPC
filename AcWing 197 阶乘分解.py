n = int(input())

N = n + 1
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

for p in primes:
    cnt = 0
    i = n
    while i:
        i //= p
        cnt += i
    print(p, cnt)


