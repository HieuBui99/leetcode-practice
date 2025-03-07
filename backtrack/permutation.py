from typing import List

def permutation(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
        
    
    backtrack([])
    return res