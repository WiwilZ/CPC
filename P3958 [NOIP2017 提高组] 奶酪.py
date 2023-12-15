class UFS:
    def __init__(self, n):
        self.fa = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        if self.rank[rootx] < self.rank[rooty]:
            self.fa[rootx] = rooty
        else:
            self.fa[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


def insect(x1, y1, z1, x2, y2, z2, r):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 <= 4 * r ** 2


def solve():
    n, h, r = map(int, input().split())
    ufs = UFS(n + 2)

    pos = []
    for i in range(n):
        x, y, z = map(int, input().split())
        if z <= r and z + r >= h:
            for _ in range(i + 1, n):
                input()
            return True
        if z <= r:
            ufs.union(i, n)
        elif z + r >= h:
            ufs.union(i, n + 1)
        for j, p in enumerate(pos):
            if insect(x, y, z, *p, r):
                ufs.union(i, j)
            if ufs.is_connected(n, n + 1):
                for _ in range(i + 1, n):
                    input()
                return True
        pos.append((x, y, z))
    return ufs.is_connected(n, n + 1)


for _ in range(int(input())):
    print('Yes' if solve() else 'No')
