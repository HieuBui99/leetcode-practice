from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    n_row = len(matrix)
    n_col = len(matrix[0])

    top_idx = 0
    bot_idx = n_row - 1
    while top_idx <= bot_idx:
        mid = (top_idx + bot_idx) // 2
        mid_row = matrix[mid]
        if target > mid_row[-1]:
            top_idx = mid + 1
        elif target < mid_row[0]:
            bot_idx = mid - 1
        else:
            break
    if not (top_idx <= bot_idx): 
        return False
    l, r = 0, n_col - 1
    while l <= r:
        m = (r + l) // 2
        if matrix[mid][m] > target:
            r = m - 1
        elif matrix[mid][m] < target:
            l = m + 1
        else:
            return True
    return False