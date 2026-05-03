def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo    

print(search_insert([1, 3, 5, 6], 5)) # → 2
print(search_insert([1, 3, 5, 6], 2)) # → 1
print(search_insert([1, 3, 5, 6], 7)) # → 4
print(search_insert([1, 3, 5, 6], 0)) # → 0
