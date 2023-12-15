from collections import defaultdict
from functools import cache


tree = defaultdict(set)
n = int(input())
for i in range(2, n + 1):
    parent = int(input())
    tree[parent].add(i)


@cache
def height(node):
    m = max((height(child) for child in tree[node]), default=0)
    return m + len(tree[node])


print(height(1))
