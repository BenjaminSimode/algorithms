from evaluateExpression import evaluate


def test_evaluate():
    cases = [
        # (input, expected, description)
        ("3+2*2",       7,   "multiplication before addition"),
        ("10/2+3",      8,   "division before addition"),
        ("2*3+4*2",     14,  "multiple multiplications"),
        ("14-3*2",      8,   "multiplication before subtraction"),
        ("6/2+1",       4,   "division before addition"),
        ("1+1",         2,   "simple addition"),
        ("10-3",        7,   "simple subtraction"),
        ("6*6",         36,  "simple multiplication"),
        ("10/2",        5,   "simple division"),
        ("2+3+4",       9,   "multiple additions"),
        ("10-3-2",      5,   "multiple subtractions"),
        ("2*3*4",       24,  "multiple multiplications"),
        ("100/2/5",     10,  "multiple divisions"),
        ("1+2*3-4/2",   5,   "all operators mixed"),
    ]

    passed = 0
    failed = 0

    for input, expected, description in cases:
        result = evaluate(input)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status} [{description}] → got {result}, expected {expected}")

    print(f"\n{passed}/{passed + failed} tests passed")


test_evaluate()
