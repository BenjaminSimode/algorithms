from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    hash_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash_map:
            return [hash_map[complement], i]

        hash_map[num] = i

    return []

print(two_sum([2, 7, 11, 15], 9))  # → [0, 1]  (car 2 + 7 = 9)
print(two_sum([3, 5, 4], 8))       # → [0, 1]  (car 3 + 5 = 8)
print(two_sum([3, 2, 4], 6))       # → [1, 2]  (car 2 + 4 = 6)
