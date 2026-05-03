from typing import List

def find_rotations(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if mid > 0 and nums[mid - 1] > nums[mid]:
            return mid
        elif nums[mid] < nums[left]:
            right = mid - 1
        else:
            left = mid + 1
    
    return 0 
    
# debug your code below
print(find_rotations([2, 3, 4, 1]))
