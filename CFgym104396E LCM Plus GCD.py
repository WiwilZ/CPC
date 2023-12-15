x, k = map(int, input().split())

if x == 1:
    print(0)
    exit()


mod = 1000000007

def quick_power(base, exponent):
    res = 1
    while exponent:
        if exponent & 1:
            res = res * base % mod
        base = base * base % mod
        exponent >>= 1
    return res


N = 10001

factorial = [1] * N
for i in range(2, N):
    factorial[i] = factorial[i - 1] * i % mod

inv_factorial = [1] * N
inv_factorial[-1] = quick_power(factorial[-1], mod - 2)
for i in range(N - 1, 2, -1):
    inv_factorial[i - 1] = inv_factorial[i] * i % mod


ans = 0

def calc(n):
    global ans
    n -= 1
    counts = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i != 0:
            continue
        cnt = 2
        n //= i
        while n % i == 0:
            cnt += 1
            n //= i
        counts.append(cnt)
        if n == 1:
            break
    if n != 1:
        counts.append(2)

    m = len(counts)
    for i in range(1 << m):
        tmpmask = 0
        tmpcounts = counts[:]
        for kk in range(m):
            if i >> kk & 1:
                tmpmask = ~tmpmask
                tmpcounts[kk] -= 1
        for j in range(1 << m):
            mask = tmpmask
            num = 1 # 总因子数
            for kk, cnt in enumerate(tmpcounts):
                if j >> kk & 1:
                    if cnt == 1:
                        break
                    mask = ~mask
                    cnt -= 1
                num *= cnt
            else:
                if num < k:
                    continue
                num = factorial[num] * inv_factorial[k] % mod * inv_factorial[num - k] % mod
                num = (num ^ mask) - mask
                ans = (ans + num) % mod

calc(x)
sq = int(x ** 0.5)
for i in range(2, sq):
    if x % i != 0:
        continue
    calc(i)
    calc(x // i)
if sq * sq == x:
    calc(sq)
elif x % sq == 0:
    calc(sq)
    calc(x // sq)

print(ans)
