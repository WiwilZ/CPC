for case in range(1, int(input()) + 1):
    n = int(input())
    ans = 0
    l = 2
    while l < n:
        tmp = n // l
        r = n // tmp
        ans += (((l + r) * (r - l + 1)) >> 1) * (tmp - 1)
        l = r + 1
    print(f'Case {case}: {ans}')
