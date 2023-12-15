from math import inf


def lowbit(x):
    return x & (-x)


class Index:
    def __init__(self, n, initial):
        N = n + 1
        self.tree1 = [0] * N
        self.tree2 = [0] * N
        pre = 0
        for i, e in enumerate(initial, start=1):
            self._update(i, e - pre)
            pre = e

    def __setitem__(self, key, x):
        i, j = key
        self._update(i, x)
        self._update(j + 1, -x)

    def __getitem__(self, key):
        i, j = key
        return self._query(j) - self._query(i - 1)

    def _update(self, i, x):
        j = i
        while i < len(self.tree1):
            self.tree1[i] += x
            self.tree2[i] += x * (j - 1)
            i += lowbit(i)

    def _query(self, i):
        j = i
        ans = 0
        while i > 0:
            ans += j * self.tree1[i] - self.tree2[i]
            i -= lowbit(i)
        return ans


class BIT:
    def __init__(self, n, initial):
        self.min_initial = [0] + list(initial)
        self.min = self.min_initial[:]
        self.max_initial = self.min_initial[:]
        self.max = self.max_initial[:]
        for i in range(1, n + 1):
            j = 1
            while j < lowbit(i):
                self.min[i] = min(self.min[i], self.min[i - j])
                self.max[i] = max(self.max[i], self.max[i - j])
                j <<= 1

    def delete(self, i):
        self.min_initial[i] = inf
        self.max_initial[i] = -inf
        while i < len(self.min):
            self.min[i] = inf
            self.max[i] = -inf
            j = 1
            while j < lowbit(i):
                self.min[i] = min(self.min[i], self.min[i - j])
                self.max[i] = max(self.max[i], self.max[i - j])
                j <<= 1
            i += lowbit(i)

    def __getitem__(self, key):
        i, j = key
        min_ans, max_ans = inf, -inf
        while j != i:
            j -= 1
            while j - i >= lowbit(j):
                min_ans = min(min_ans, self.min[j])
                max_ans = max(max_ans, self.max[j])
                j -= lowbit(j)
            min_ans = min(min_ans, self.min_initial[j])
            max_ans = max(max_ans, self.max_initial[j])
        return min_ans, max_ans


n, m = map(int, input().split())
bit = BIT(n, map(int, input().split()))
for _ in range(m):
    z, *args = map(int, input().split())
    if z == 1:
        bit.delete(*args)
    else:
        print(*bit[args])
