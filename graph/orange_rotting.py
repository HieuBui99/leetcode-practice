from typing import List
from collections import deque


def oranges_rotting(grid: List[List[int]]) -> int:
    n_row = len(grid)
    n_col = len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    fresh = 0
    q = deque()
    seen = set()
    for r in range(n_row):
        for c in range(n_col):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append((r, c)) 
                seen.add((r, c))
    minutes = 0
    while fresh > 0 and q:
        minutes += 1
        for _ in range(len(q)):
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n_row and 0 <= nc < n_col and (nr, nc) not in seen and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    seen.add((nr, nc))
                    q.append((nr, nc))
                    fresh -= 1
    
    if fresh == 0:
        return minutes
    else:
        return -1