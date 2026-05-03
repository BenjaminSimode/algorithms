def find_first_last(nums: list[int], target: int) -> list[int]:
    return [
        find_bound(nums, target, left=True),
        find_bound(nums, target, left=False)
    ]

def find_bound(nums: list[int], target: int, left: bool) -> int:
    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = (high + low) // 2

        if nums[mid] == target:
            result = mid
            if left:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

print(find_first_last([5, 7, 7, 8, 8, 10], 8)) # → [3, 4]
print(find_first_last([5, 7, 7, 8, 8, 10], 6)) # → [-1, -1]
print(find_first_last([1, 1, 1, 1], 1))        # → [0, 3]
print(find_first_last([], 0))                  # → [-1, -1]
