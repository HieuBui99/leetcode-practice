from typing import List
from collections import deque

def islands_and_treasure(self, grid: List[List[int]]) -> None:
    inf = 2147483647
    n_row = ROWS = len(grid)
    n_col = COLS = len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r in range(n_row):
        for c in range(n_col):
            if grid[r][c] == inf:
                q = deque([(r, c)])
                visit = [[False] * COLS for _ in range(ROWS)]
                visit[r][c] = True
                steps = 0
                while q:
                    for _ in range(len(q)):
                        row, col = q.popleft()
                        if grid[row][col] == 0:
                            grid[r][c] = steps
                            break
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if (0 <= nr < ROWS and 0 <= nc < COLS and 
                                not visit[nr][nc] and grid[nr][nc] != -1
                            ):
                                visit[nr][nc] = True
                                q.append((nr, nc))
                    if grid[r][c] == steps:
                        break
                    steps += 1