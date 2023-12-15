mod = 9901

def fast_pow(x, exp):
    ans = 1
    while exp:
        if exp & 1:
            ans = ans * x % mod
        x = x * x % mod
        exp >>= 1
    return ans


a, b = map(int, input().split())
if a <= 1:
    print(a)
elif a == 2:
    print(fast_pow(2, b + 1) - 1)
else:
    ans = 1
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            k = 1
            a //= i
            while a % i == 0:
                k += 1
                a //= i
            cnt = (fast_pow(i, k * b + 1) - 1) * fast_pow(i - 1, mod - 2) % mod
            ans = ans * cnt % mod
            if a == 1:
                break
    if a != 1:
        cnt = b + 1
        if (a - 1) % mod:
            cnt = (fast_pow(a, cnt) - 1) * fast_pow(a - 1, mod - 2) % mod
        ans = ans * cnt % mod
    print(ans)
