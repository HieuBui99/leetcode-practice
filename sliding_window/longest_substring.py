def length_of_longest_substring(s):
    if len(s) <= 1:
        return len(s)
    store = set()
    longest = 1
    start = 0
    end = 1
    store.add(s[start])
    while end < len(s):
        if s[end] not in store:
            longest = max(longest, end - start + 1)
            store.add(s[end])
            end += 1
        else:
            store.remove(s[start])
            start += 1
    
    return longest