mod = 998244353

n, a0, x, y, m, K = map(int, input().split())

a = [a0]
pre0, pre1 = a0, a0
for _ in range(1, n):
    pre0 = (pre0 * x + y) % m
    pre1 = (pre1 + pre0) % mod
    a.append((a[-1] + pre1) % mod)

for k in range(1, K):
    pre, a[k - 1] = a[k - 1], 0
    for i in range(k, n):
        tmp, pre = pre, a[i]
        a[i] = (tmp + a[i - 1]) % mod

ans = 0
for i in range(K - 1, n):
    ans ^= a[i] * (i + 1)
print(ans)
