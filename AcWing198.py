n = int(input())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
ans = int(2e9)
cnt_ans = 1


def dfs(idx, cur, cnt, p):
    global ans, cnt_ans
    if idx == 10:
        if cnt > cnt_ans or cnt == cnt_ans and cur < ans:
            ans = cur
            cnt_ans = cnt
        return
    for i in range(1, p + 1):
        if cur * primes[idx] > n:
            return
        cur *= primes[idx]
        dfs(idx + 1, cur, cnt * (i + 1), i)


dfs(0, 1, 1, 31)
print(ans)
