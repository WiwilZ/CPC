n = int(input())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

ans = 1000000000000000000

def dfs(idx, cur, cnt, p):
    global ans
    if cnt > n or idx == 15:
        return
    if cnt == n:
        ans = cur
        return
    for i in range(1, p + 1):
        t = cur * primes[idx]
        if t > ans:
            return
        cur = t
        dfs(idx + 1, cur, cnt * (i + 1), i)

dfs(0, 1, 1, 59)
print(ans)

