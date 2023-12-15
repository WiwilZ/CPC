# import math

# input()
# ls = map(int, input().split())
# cs = map(int, input().split())

# dp = {0: 0}
# for l, c in zip(ls, cs):
#     for k, v in list(dp.items()):
#         x = math.gcd(k, l)
#         dp[x] = min(dp.get(x, math.inf), v + c)
# print(dp.get(1, -1))


import math
import heapq

n = int(input())
ls = list(map(int, input().split()))
cs = list(map(int, input().split()))

heap = [(0, 0)]
visited = set()
dist = {0: 0}

while heap:
    u = heapq.heappop(heap)[1]
    if u == 1:
        break
    if u in visited:
        continue
    visited.add(u)
    for l, c in zip(ls, cs):
        v = math.gcd(u, l)
        if v in visited or v in dist and dist[v] <= dist[u] + c:
            continue
        dist[v] = dist[u] + c
        heapq.heappush(heap, (dist[v], v))

print(dist.get(1, -1))
