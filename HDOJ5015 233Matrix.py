mod = 10000007


def mat_mul(A, B):
    return [[sum(a * b % mod for a, b in zip(row, col)) % mod for col in zip(*B)] for row in A]


def mat_pow(A, n):
    res = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(res)):
        res[i][i] = 1
    while n:
        if n & 1:
            res = mat_mul(res, A)
        A = mat_mul(A, A)
        n >>= 1
    return res


while True:
    try:
        n, m = map(int, input().split())
        A = [[10] + [1] * i + [0] * (n - i) + [1] for i in range(n + 1)] + [[0] * (n + 1) + [1]]
        A = mat_pow(A, m)
        ans = (A[n][0] * 23 % mod + sum(a * b % mod for a, b in zip(A[n][1:-1], map(int, input().split()))) + A[n][-1] * 3 % mod) % mod
        print(ans)
    except:
        break
