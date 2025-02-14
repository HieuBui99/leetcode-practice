from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    """
    Explaination:
    - We need to find a path in the board that spells out the word
    - We can start at any cell in the board
    - We can move to any of the 4 adjacent cells (up, down, left, right)
    - We can't visit the same cell more than once
    - We can't use the same letter more than once
    - We can't move outside the board
    - We can't move diagonally
    - We can't move to a cell that has been visited
    - We can't move to a cell that doesn't have the next letter in the word
    - If we reach the end of the word, we have found a path
    - We can use backtracking to explore all possible paths
    - We can use a set to keep track of visited cells
    - We can use a recursive function to explore all possible paths
    - We can use a loop to start the recursive function at every cell in the board
    - If the recursive function returns True, we have found a path
    """
    n_row = len(board)
    n_col = len(board[0])
    visited = set()
    def backtrack(r, c, i):
        if i == len(word):
            return True

        if min(r, c) < 0 or r >= n_row or c >= n_col or word[i] != board[r][c] or (r, c) in visited:
            return False

        visited.add((r, c))
        res = (backtrack(r+1, c, i+1) or
                backtrack(r-1, c, i+1) or
                backtrack(r, c+1, i+1) or 
                backtrack(r, c-1, i+1))
        visited.remove((r, c))
        return res

    for r in range(n_row):
        for c in range(n_col):
            if backtrack(r, c, 0): 
                return True

    return False