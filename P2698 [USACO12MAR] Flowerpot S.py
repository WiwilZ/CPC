from collections import deque
from sys import maxsize

n, d = map(int, input().split())
ps = sorted((tuple(map(int, input().split())) for _ in range(n)), key=lambda x: x[0])

ans = maxsize
qmax, qmin = deque(), deque()
l = 0
for r, (x, y) in enumerate(ps):
    while qmax and ps[qmax[-1]][1] < y:
        qmax.pop()
    qmax.append(r)
    while qmin and ps[qmin[-1]][1] > y:
        qmin.pop()
    qmin.append(r)

    while l <= r and ps[qmax[0]][1] - ps[qmin[0]][1] >= d:
        ans = min(ans, x - ps[l][0])
        l += 1
        while qmax and qmax[0] < l:
            qmax.popleft()
        while qmin and qmin[0] < l:
            qmin.popleft()

print(ans if ans != maxsize else -1)
