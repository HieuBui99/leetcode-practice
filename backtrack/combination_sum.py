from typing import List

def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    def backtrack(i, combination):
        cur_sum = sum(combination)
        if cur_sum == target:
            res.append(combination.copy())
            return
        if cur_sum > target or i >= len(nums):
            return

        combination.append(nums[i])
        backtrack(i, combination)
        combination.pop()
        backtrack(i+1, combination)

    backtrack(0, [])
    return res
