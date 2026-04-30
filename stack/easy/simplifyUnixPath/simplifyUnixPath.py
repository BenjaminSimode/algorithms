def simplify(path: str) -> str:
    pass  # your code goes here



print(simplify("/home/../usr/./bin"))  # → "/usr/bin"
print(simplify("/a/./b/../../c/"))     # → "/c"
print(simplify("/../"))                # → "/"
print(simplify("/home//foo/"))         # → "/home/foo"
print(simplify("/"))                   # → "/"
