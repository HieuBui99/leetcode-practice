from typing import List

def num_islands(grid: List[List[str]]) -> int:
    n_row = len(grid)
    n_col = len(grid[0])
    n_island = 0
    for r in range(n_row):
        for c in range(n_col):
            if grid[r][c] == "1":
                print(r,c )
                n_island += 1
                stack = []
                stack.append((r, c))
                while stack:
                    cur_row, cur_col = stack.pop()
                    if grid[cur_row][cur_col] == "1":
                        grid[cur_row][cur_col] = "0"

                        if cur_row - 1 >= 0:
                            stack.append((cur_row-1, cur_col))
                        if cur_row + 1 < n_row:
                            stack.append((cur_row+1, cur_col))
                        if cur_col -1 >= 0:
                            stack.append((cur_row, cur_col-1))
                        if cur_col + 1 < n_col:
                            stack.append((cur_row, cur_col+1))

    return n_island 