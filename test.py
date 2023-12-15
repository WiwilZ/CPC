class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        n = len(nums)

        next_idx = [n] * n
        stack = []
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                stack.pop()
            if stack:
                next_idx[j] = stack[-1]
            stack.append(j)

        prev_idx = [-1] * n
        stack = []
        for j in range(n):
            while stack and nums[j] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                prev_idx[j] = stack[-1]
            stack.append(j)

        res = []
        i = 0
        while i < n - 3 and nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] <= target:
            if nums[i] + nums[-3] + nums[-2] + nums[-1] >= target:
                j = i + 1
                while j < n - 2 and nums[i] + nums[j] + nums[j + 1] + nums[j + 2] <= target:
                    l, r = j + 1, n - 1
                    while l < r:
                        s = nums[i] + nums[j] + nums[l] + nums[r]
                        if s == target:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            l, r = next_idx[l], prev_idx[r]
                        elif s < target:
                            l += 1
                        else:
                            r -= 1
                    j = next_idx[j]
            i = next_idx[i]
        return res
