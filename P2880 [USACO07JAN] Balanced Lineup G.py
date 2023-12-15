# from math import inf
#
#
# def lowbit(x):
#     return x & -x
#
#
# def build(i):
#     x = nums[i]
#     while i <= n:
#         treemax[i] = max(treemax[i], x)
#         treemin[i] = min(treemin[i], x)
#         i += lowbit(i)
#
#
# def query(l, r):
#     maxans = 0
#     minans = inf
#     while r >= l:
#         maxans = max(maxans, nums[r])
#         minans = min(minans, nums[r])
#         r -= 1
#         while r >= l + lowbit(r):
#             maxans = max(maxans, treemax[r])
#             minans = min(minans, treemin[r])
#             r -= lowbit(r)
#     return maxans - minans
#
#
# n, q = map(int, input().split())
# treemax = [0] * (n + 1)
# treemin = [inf] * (n + 1)
#
# nums = [0]
# for i in range(1, n + 1):
#     nums.append(int(input()))
#     build(i)
#
# for _ in range(q):
#     l, r = map(int, input().split())
#     print(query(l, r))


n, q = map(int, input().split())
N = n + 1
Log2N = 17
maxs = [[0] * Log2N for _ in range(N)]
mins = [[0] * Log2N for _ in range(N)]

log2 = [0] * N
for i in range(2, N):
    log2[i] = log2[i >> 1] + 1

for i in range(1, N):
    maxs[i][0] = int(input())
    mins[i][0] = maxs[i][0]

for j in range(1, Log2N):
    for i in range(1, N - (1 << j) + 1):
        maxs[i][j] = max(maxs[i][j - 1], maxs[i + (1 << (j - 1))][j - 1])
        mins[i][j] = min(mins[i][j - 1], mins[i + (1 << (j - 1))][j - 1])

for _ in range(q):
    l, r = map(int, input().split())
    s = log2[r - l + 1]
    print(max(maxs[l][s], maxs[r - (1 << s) + 1][s]) - min(mins[l][s], mins[r - (1 << s) + 1][s]))
