def lowbit(x):
    return x & -x


def build(i, x):
    while i <= n:
        tree[i] = max(tree[i], x)
        i += lowbit(i)


def query(i):
    ans = 0
    while i > 0:
        ans = max(ans, tree[i])
        i -= lowbit(i)
    return ans


n, d = map(int, input().split())
nums = [0] * (n + 1)
tree = [0] * (n + 1)
i = n
t = 0
for _ in range(n):
    op, x = input().split()
    x = int(x)
    if op == 'A':
        build(i, (x + t) % d)
        i -= 1
    else:
        t = query(i + x)
        print(t)
