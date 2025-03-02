from typing import List
from collections import deque

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    n_row = len(heights)
    n_col = len(heights[0])

    res = []

    pacific = set()
    atlantic = set()

    for r in range(n_row):
        pacific.add((r, 0))
        atlantic.add((r, n_col-1))
    
    for c in range(n_col):
        pacific.add((0, c))
        atlantic.add((n_row-1, c))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    in_pac = [[False]*n_col for _ in range(n_row)]
    in_atl = [[False]*n_col for _ in range(n_row)]

    def bfs(source, in_ocean):
        q = deque(source)
        while q:
            row, col = q.popleft()
            in_ocean[row][col] = True

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n_row and 0 <= nc < n_col and not in_ocean[nr][nc] and heights[row][col] <= heights[nr][nc]:
                    q.append((nr, nc))

    bfs(pacific, in_pac)
    bfs(atlantic, in_atl)

    for r in range(n_row):
        for c in range(n_col):
            if in_pac[r][c] and in_atl[r][c]:
                res.append([r, c])

    return res