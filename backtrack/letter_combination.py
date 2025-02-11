from typing import List

def letter_combinations(digits: str) -> List[str]:
    res = []
    hash_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, combination):
        if i == len(digits):
            if combination:
                res.append(combination)
            return

        for char in hash_map[digits[i]]:
            combination = combination + char
            backtrack(i+1, combination)
            combination = combination[:-1]

    
    backtrack(0, "")

    return res