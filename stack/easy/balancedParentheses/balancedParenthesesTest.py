from balancedParentheses import isBalanced

def test_isBalanced():
    cases = [
        # (input, expected, description)
        ("",        True,  "empty string"),
        ("(())",    True,  "nested parens"),
        ("()[]{}",  True,  "multiple types"),
        ("(]",      False, "wrong closing bracket"),
        ("([)]",    False, "interleaved brackets"),
        ("{[]}",    True,  "nested mixed"),
        ("(((",     False, "unclosed brackets"),
        ("}}",      False, "no opening bracket"),
        ("([{}])",  True,  "deeply nested"),
    ]

    passed = 0
    failed = 0

    for input, expected, description in cases:
        result = isBalanced(input)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status} [{description}] → got {result}, expected {expected}")

    print(f"\n{passed}/{passed + failed} tests passed")

test_isBalanced()
