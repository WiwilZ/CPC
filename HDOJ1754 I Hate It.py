def lowbit(x):
    return x & -x


def build(i):
    x = nums[i]
    while i <= n:
        tree[i] = max(tree[i], x)
        i += lowbit(i)


def update(i):
    while i <= n:
        tree[i] = nums[i]
        j = 1
        while j < lowbit(i):
            tree[i] = max(tree[i], tree[i - j])
            j <<= 1
        i += lowbit(i)


def query(l, r):
    ans = 0
    while r >= l:
        ans = max(ans, nums[r])
        r -= 1
        while r >= l + lowbit(r):
            ans = max(ans, tree[r])
            r -= lowbit(r)
    return ans


n, m = map(int, input().split())

tree = [0] * (n + 1)
nums = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    build(i)

for _ in range(m):
    op, *args = input().split()
    x, y = map(int, args)
    if op == 'U':
        nums[x] = y
        update(x)
    else:
        print(query(x, y))
