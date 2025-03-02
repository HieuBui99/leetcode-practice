from typing import List
from collections import deque


def surrounded_region(board: List[List[str]]) -> None:
    n_row, n_col = len(board), len(board[0])

    q = deque()
    for r in range(n_row):
        for c in range(n_col):
            if (r==0 or r==n_row-1 or c==0 or c==n_col-1) and board[r][c] == "O":
                q.append((r, c))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c = q.popleft()
        board[r][c] = "T"
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n_row and 0 <= nc < n_col and board[nr][nc] == "O":
                q.append((nr, nc))
    
    for r in range(n_row):
        for c in range(n_col):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"