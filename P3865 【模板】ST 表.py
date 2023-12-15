n, m = map(int, input().split())
N = n + 1
log2N = 17
f = [[0] * log2N for _ in range(N)]
log2 = [0] * N
for i in range(2, N):
    log2[i] = log2[i >> 1] + 1

for i, num in enumerate(map(int, input().split()), 1):
    f[i][0] = num

for j in range(1, log2N):
    for i in range(1, N - (1 << j) + 1):
        f[i][j] = max(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])

for _ in range(m):
    l, r = map(int, input().split())
    s = log2[r - l + 1]
    print(max(f[l][s], f[r - (1 << s) + 1][s]))
