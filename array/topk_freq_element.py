from typing import List


def topk_frequent(nums: List[int], k: int) -> List[int]:
        """
        - Count the frequency of each element.
        - Store the elements in a list based on their frequency.
        - Loop through the list and append the elements to the result list until the length of the result list is equal to k.
        """
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)

        res = []
        freq_idx = len(freq) - 1
        while len(res) < k:
            for num in freq[freq_idx]:
                if len(res) < k:
                    res.append(num)
            freq_idx -= 1


        return res