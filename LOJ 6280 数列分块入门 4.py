def lowbit(x):
    return x & -x


def _add(i, x):
    j = i
    while i <= n:
        tree1[i] += x
        tree2[i] += x * (j - 1)
        i += lowbit(i)


def add(l, r, x):
    _add(l, x)
    _add(r + 1, -x)


def _query(i):
    ans = 0
    j = i
    while i > 0:
        ans += j * tree1[i] - tree2[i]
        i -= lowbit(i)
    return ans


def query(l, r):
    return _query(r) - _query(l - 1)


n = int(input())
tree1 = [0] * (n + 1)
tree2 = [0] * (n + 1)
last = 0
for i, num in enumerate(map(int, input().split()), 1):
    _add(i, num - last)
    last = num

for _ in range(n):
    op, l, r, c = map(int, input().split())
    if op == 0:
        add(l, r, c)
    else:
        print(query(l, r) % (c + 1))
