from dailyTemperatures import dailyTemperatures

def test_dailyTemperatures():
    cases = [
        # (input, expected, description)
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0], "standard case"),
        ([30, 40, 50, 60],                 [1, 1, 1, 0],               "strictly increasing"),
        ([60, 50, 40, 30],                 [0, 0, 0, 0],               "strictly decreasing"),
        ([30, 20, 10],                     [0, 0, 0],                  "no warmer day"),
        ([10, 10, 10],                     [0, 0, 0],                  "all same temperature"),
        ([50],                             [0],                        "single element"),
        ([50, 60],                         [1, 0],                     "two elements warmer"),
        ([60, 50],                         [0, 0],                     "two elements colder"),
        ([70, 60, 80, 50, 90],             [2, 1, 2, 1, 0],           "mixed case"),
    ]

    passed = 0
    failed = 0

    for input, expected, description in cases:
        result = dailyTemperatures(input)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status} [{description}] → got {result}, expected {expected}")

    print(f"\n{passed}/{passed + failed} tests passed")

test_dailyTemperatures()
