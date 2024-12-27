from collections import defaultdict

def character_replacement(s: str, k: int) -> int:
    if len(s) <= 1:
        return len(s)

    l, r = 0, 1
    counter = defaultdict(int)
    counter[s[l]] = 1
    res = 0
    while r <= len(s) - 1:
        counter[s[r]] += 1
        most_freq = max(counter.values())
        n_replacement = r - l + 1 - most_freq

        if n_replacement <= k:
            res = max(res, r - l + 1)
        else:
            counter[s[l]] -= 1
            l += 1
        r += 1
    return res
