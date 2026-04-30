from simplifyUnixPath import simplify

def test_simplify():
    cases = [
        # (input, expected, description)
        ("/home/../usr/./bin",   "/usr/bin",   "parent + current dir"),
        ("/a/./b/../../c/",      "/c",         "multiple parent traversals"),
        ("/../",                 "/",          "cannot go above root"),
        ("/home//foo/",          "/home/foo",  "double slash"),
        ("/",                    "/",          "root only"),
        ("/a/b/c",               "/a/b/c",     "simple path no change"),
        ("/a/b/c/../../d",       "/a/d",       "partial traversal"),
        ("/..hidden",            "/..hidden",  "hidden file with dots"),
        ("/home/./.",             "/home",      "multiple current dirs"),
        ("//a//b//c//",          "/a/b/c",     "multiple double slashes"),
    ]

    passed = 0
    failed = 0

    for input, expected, description in cases:
        result = simplify(input)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status} [{description}] → got '{result}', expected '{expected}'")

    print(f"\n{passed}/{passed + failed} tests passed")


test_simplify()
