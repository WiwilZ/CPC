# 背包问题
## 组合种类数问题

- [力扣 377 组合总和 Ⅳ](https://leetcode.cn/problems/combination-sum-iv/)
- [力扣 494 目标和](https://leetcode.cn/problems/target-sum/)

```python
dp = [1] + [0] * target

dp[i] += dp[i - num]
```
## 判断问题

- [力扣 139 单词拆分](https://leetcode.cn/problems/word-break/)

- [力扣 416 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

```python
dp = [True] + [False] * target
dp[i] |= dp[i - num]
```
## 最大最小问题

- [力扣 279 完全平方数](https://leetcode.cn/problems/perfect-squares/)
- [力扣 322 零钱兑换](https://leetcode.cn/problems/coin-change/)

```python
dp = [0] + [inf] * target
dp[i] = min(dp[i], dp[i - num] + 1)

dp = [0] * (target + 1)
dp[i] = max(dp[i], dp[i - num] + 1)
```
## 0-1背包问题——元素不可重复使用

- [力扣 416 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)
- [力扣 494 目标和](https://leetcode.cn/problems/target-sum/)

```python
for num in nums:
    for i in range(target, num - 1, -1):
```
## 完全背包问题——元素可重复使用

- [力扣 279 完全平方数](https://leetcode.cn/problems/perfect-squares/)
- [力扣 322 零钱兑换](https://leetcode.cn/problems/coin-change/)

```python
for num in nums:
    for i in range(num, target + 1):
```
## 考虑元素顺序

- [力扣 139 单词拆分](https://leetcode.cn/problems/word-break/)

- [力扣 377 组合总和 Ⅳ](https://leetcode.cn/problems/combination-sum-iv/)

```python
for i in range(1, target + 1):
    for num in nums:
```