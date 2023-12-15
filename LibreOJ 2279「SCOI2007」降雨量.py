import bisect
from math import inf

n = int(input())
N = n + 1
log2 = [0] * N
for i in range(2, N):
    log2[i] = log2[i >> 1] + 1
Log2N = log2[n] + 2
f = [[0] * Log2N for _ in range(N)]

maps = []
for i in range(1, n + 1):
    y, r = map(int, input().split())
    f[i][0] = r
    maps.append((i, y, r))

for j in range(1, Log2N):
    for i in range(1, N - (1 << j) + 1):
        f[i][j] = max(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])


def solve(y, x):
    pl = bisect.bisect_left(maps, y, key=lambda t: t[1])
    pr = bisect.bisect_left(maps, x, key=lambda t: t[1])

    lexists = pl < len(maps) and maps[pl][1] == y
    rexists = pr < len(maps) and maps[pr][1] == x

    if not lexists and not rexists:
        return 'maybe'

    if lexists and rexists:
        lval = maps[pl][2]
        rval = maps[pr][2]
        l = maps[pl + 1][0]
        r = maps[pr - 1][0]
        if r < l:
            midval = -inf
        else:
            s = log2[r - l + 1]
            midval = max(f[l][s], f[r - (1 << s) + 1][s])
        if not midval < rval <= lval:
            return 'false'
        if x - y == r - l + 2:
            return 'true'
        return 'maybe'

    if pl == len(maps) - 1 or pr == 0:
        return 'maybe'

    if lexists:
        val = maps[pl][2]
        l = maps[pl + 1][0]
    else:
        val = maps[pr][2]
        l = maps[pl][0]
    r = maps[pr - 1][0]
    if r >= l:
        s = log2[r - l + 1]
        midval = max(f[l][s], f[r - (1 << s) + 1][s])
        if val <= midval:
            return 'false'
    return 'maybe'


for _ in range(int(input())):
    y, x = map(int, input().split())
    print(solve(y, x))
