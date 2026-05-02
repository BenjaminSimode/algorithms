from twoSum import two_sum

def test_two_sum():
    cases = [
        # (nums, target, expected, description)
        ([2, 7, 11, 15], 9,  [0, 1], "classic case"),
        ([3, 2, 4],      6,  [1, 2], "non-adjacent pair"),
        ([3, 3],         6,  [0, 1], "same value twice"),
        ([1, 2, 3, 4],   7,  [2, 3], "last two elements"),
        ([0, 4, 3, 0],   0,  [0, 3], "two zeros"),
        ([-1, -2, -3],   -5, [1, 2], "negative numbers"),
        ([1, 5, -3, 8],  5,  [2, 3], "negative and positive mix"),
        ([10, 20, 30],   50, [1, 2], "larger values"),
    ]

    passed = 0
    failed = 0

    for nums, target, expected, description in cases:
        result = two_sum(nums, target)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status} [{description}] twoSum({nums}, {target}) → got {result}, expected {expected}")

    print(f"\n{passed}/{passed + failed} tests passed")

test_two_sum()
