from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    - Create a dictionary to store the index of the elements.
    - Loop through the list and check if the difference between the target and the current element is in the dictionary.
    - If it is, return the indices of the two elements.
    """
    num_dict = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_dict:
            return [num_dict[diff], i]
        num_dict[num] = i
    return []