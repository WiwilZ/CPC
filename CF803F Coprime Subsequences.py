mod = 1000000007

N = 100001

is_prime = [True] * N
primes = []

mu = [0] * N
mu[1] = 1

pow2 = [1] * N
pow2[1] = 2

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
    pow2[i] = (pow2[i - 1] << 1) % mod


n = int(input())

maxa = 0
cnt = [0] * N
for a in map(int, input().split()):
    maxa = max(maxa, a)
    cnt[a] += 1

ans = pow2[n] - 1
for i in range(2, maxa + 1):
    num = 0
    for j in range(i, maxa + 1, i):
        num = (num + cnt[j]) % mod
    ans = (ans + mu[i] * (pow2[num] - 1)) % mod
print(ans)
