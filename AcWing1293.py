n = int(input())

is_prime = [True] * (n + 2)
primes = []
for i in range(2, n + 2):
    if is_prime[i]:
        primes.append(i)
    for e in primes:
        num = i * e
        if num > n + 1:
            break
        is_prime[num] = False
        if i % e == 0:
            break

print(1 if n <= 2 else 2)
for i in range(2, n + 2):
    print(1 if is_prime[i] else 2, end=' ')
print()
