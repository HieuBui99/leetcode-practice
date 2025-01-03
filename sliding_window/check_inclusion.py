def check_inclusion(s1: str, s2: str)-> bool:
    if len(s1) > len(s2):
        return False
    count_s1 = {}
    for c in s1:
        count_s1[c] = 1 + count_s1.get(c, 0)

    for i in range(0, len(s2) - len(s1)+1):
        count_s2 = {}
        for c in s2[i:i+len(s1)]:
            count_s2[c] = 1 + count_s2.get(c, 0)
        if count_s1 == count_s2:
            return True
    
    return False
