# Evaluate Expression

## Problem

Given a string representing a basic arithmetic expression, evaluate it and return the result as an integer.

Supported operators: `+`, `-`, `*`, `/`
- No parentheses
- Integer division truncates toward zero
- The expression is always valid

## Examples

```
evaluate("3+2*2")    → 7
evaluate("10/2+3")   → 8
evaluate("2*3+4*2")  → 14
evaluate("14-3*2")   → 8
evaluate("6/2+1")    → 4
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` contains only digits, `+`, `-`, `*`, `/` and spaces
- All intermediate results fit in a 32-bit integer

## Hints

<details>
<summary>Hint 1</summary>
The main challenge is operator precedence: `*` and `/` must be evaluated before `+` and `-`.
</details>

<details>
<summary>Hint 2</summary>
What if you handle `*` and `/` immediately when you see them, and defer `+` and `-` for later?
</details>

<details>
<summary>Hint 3</summary>
Store intermediate results in a stack. At the end, sum everything in the stack.
</details>

## Approach

Ask yourself these questions before coding:
1. How do you handle operator precedence without parentheses?
2. What do you push on the stack — numbers or results?
3. When do you apply the operator?
4. How do you get the final result from the stack?

## Complexity Target

| | Target |
|---|---|
| Time | O(n) |
| Space | O(n) |
