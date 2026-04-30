# Balanced Parentheses

## Problem

Given a string containing only the characters `(`, `)`, `{`, `}`, `[` and `]`, write a function to determine if the input string is valid.

A string is valid if:
- Every opening bracket has a corresponding closing bracket
- Brackets are closed in the correct order

## Examples

```
isBalanced("(())")    → true
isBalanced("()[]{}")  → true
isBalanced("(]")      → false
isBalanced("([)]")    → false
isBalanced("{[]}")    → true
isBalanced("(((")     → false
```

## Constraints

- The string can be empty → return `true`
- The string only contains bracket characters
- `1 <= s.length <= 10^4`

## Hints

<details>
<summary>Hint 1</summary>
Think about what you need to remember when you encounter an opening bracket.
</details>

<details>
<summary>Hint 2</summary>
When you encounter a closing bracket, what should the last opening bracket have been?
</details>

<details>
<summary>Hint 3</summary>
A stack is perfect for remembering the "last seen" opening bracket.
</details>

## Approach

Ask yourself these questions before coding:
1. What do I store in the stack?
2. When do I push?
3. When do I pop?
4. What is the success/failure condition at the end?

## Complexity Target

| | Target |
|-------|------|
| Time  | O(n) |
| Space | O(n) |
