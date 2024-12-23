from typing import List


def search_rotated_sorted_array(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        # left sorted 
        if nums[mid] >= nums[l]:
            if (nums[mid] < target) or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if (nums[mid] > target) or target > nums[r]:
                r = mid - 1
            else: 
                l = mid + 1
        
    return -1