from typing import List

def subset(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(i, subset):
        if i >= len(nums):
            res.append(subset.copy()) #append a copy instead of a reference
            return
        
        subset.append(nums[i])
        backtrack(i+1, subset)
        subset.pop()
        backtrack(i+1, subset)

    backtrack(0, [])
    return res


def subset2(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    def backtrack(i, subset):
        if i >= len(nums):
            res.append(subset.copy())
            return 
        subset.append(nums[i])
        backtrack(i+1, subset)
        subset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(i+1, subset)

    backtrack(0, [])
    return res