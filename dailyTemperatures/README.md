# Daily Temperatures

## Problem

Given an array of daily temperatures, return an array where each index `i` contains the number of days you would have to wait until a warmer temperature. If there is no future warmer day, put `0` for that index.

## Examples

```
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
output →       [ 1,  1,  4,  2,  1,  1,  0,  0]
```

Explanation:
- Day 0 (73°): next warmer day is day 1 (74°) → wait 1 day
- Day 2 (75°): next warmer day is day 6 (76°) → wait 4 days
- Day 6 (76°): no warmer day after → 0
- Day 7 (73°): no warmer day after → 0

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Hints

<details>
<summary>Hint 1</summary>
A brute force O(n²) solution works but is too slow. Can you do it in O(n)?
</details>

<details>
<summary>Hint 2</summary>
What if you store indices in the stack instead of temperatures?
</details>

<details>
<summary>Hint 3</summary>
When you find a warmer temperature, you can resolve all previous days that were waiting for it.
</details>

## Approach

Ask yourself these questions before coding:
1. What do I store in the stack — values or indices?
2. When do I push?
3. When do I pop, and what do I do with the popped value?
4. What does an element remaining in the stack at the end mean?

## Complexity Target

| | Target |
|---|---|
| Time | O(n) |
| Space | O(n) |
