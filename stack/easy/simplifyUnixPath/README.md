# Simplify Unix Path

## Problem

Given an absolute Unix file path, simplify it to its canonical form.

Rules:
- `.` refers to the current directory → ignore it
- `..` refers to the parent directory → go one level up
- Multiple consecutive slashes `//` are treated as a single slash
- The result must always start with `/`
- The result must not end with `/` (unless it is the root)

## Examples

```
simplify("/home/../usr/./bin")  → "/usr/bin"
simplify("/a/./b/../../c/")     → "/c"
simplify("/../")                → "/"
simplify("/home//foo/")         → "/home/foo"
simplify("/")                   → "/"
simplify("/a/b/c")              → "/a/b/c"
```

## Constraints

- `1 <= path.length <= 3000`
- The path consists of English letters, digits, `.`, `/` or `_`
- The path is a valid absolute Unix path

## Hints

<details>
<summary>Hint 1</summary>
Split the path by `/` to get individual components. Some will be empty strings — ignore them.
</details>

<details>
<summary>Hint 2</summary>
Use a stack to build the canonical path. Each valid directory name gets pushed.
</details>

<details>
<summary>Hint 3</summary>
When you encounter `..`, pop from the stack (if not empty). When you encounter `.` or `""`, do nothing.
</details>

## Approach

Ask yourself these questions before coding:
1. How do you split and clean the path components?
2. What are the 4 possible cases for each component?
3. When do you push / pop / ignore?
4. How do you reconstruct the final path from the stack?

## Complexity Target

| | Target |
|---|---|
| Time | O(n) |
| Space | O(n) |