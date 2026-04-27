# Remove Adjacent Duplicates in String

## Problem

Given a string `s` and an integer `k`, remove all groups of `k` adjacent duplicate characters. Repeat the process until no more removals are possible.

## Examples

```txt
s = 'abcd',                 k = 2  → 'abcd'
s = 'deeedbbcccbdaa',       k = 3  → 'aa'
s = 'pbbcggttciiippooaais', k = 2  → 'ps'
s = 'aaabbbacd',            k = 3  → 'acd'
```

Explanation for `'deeedbbcccbdaa'` with `k = 3`:

```
'deeedbbcccbdaa'
→ remove 'eee'  → 'dbbcccbdaa'
→ remove 'ccc'  → 'dbbdaa'    (wait, now 'bb' only has 2... but k=3, skip)
→ no more groups of 3
→ 'aa'
```

Wait — full trace:

```
'd' → stack: [(d,1)]
'e' → stack: [(d,1)(e,1)]
'e' → stack: [(d,1)(e,2)]
'e' → stack: [(d,1)(e,3)] → pop → [(d,1)]
'd' → stack: [(d,2)]
'b' → stack: [(d,2)(b,1)]
'b' → stack: [(d,2)(b,2)]
'c' → stack: [(d,2)(b,2)(c,1)]
'c' → stack: [(d,2)(b,2)(c,2)]
'c' → stack: [(d,2)(b,2)(c,3)] → pop → [(d,2)]    ← 'bb' merges with nothing
'b' → stack: [(d,2)(b,1)]                           ← new 'b', counter resets
'd' → stack: [(d,2)(b,1)(d,1)]
'a' → stack: [(d,2)(b,1)(d,1)(a,1)]
'a' → stack: [(d,2)(b,1)(d,1)(a,2)]

result: 'dd' + 'b' + 'd' + 'aa' = 'ddbdaa'  ← Hmm, let's recheck...
```

Corrected full trace for `'deeedbbcccbdaa'` with `k = 3`:

```
'd' → [(d,1)]
'e' → [(d,1)(e,1)]
'e' → [(d,1)(e,2)]
'e' → [(d,1)(e,3)] → pop → [(d,1)]
'd' → [(d,2)]
'b' → [(d,2)(b,1)]
'b' → [(d,2)(b,2)]
'c' → [(d,2)(b,2)(c,1)]
'c' → [(d,2)(b,2)(c,2)]
'c' → [(d,2)(b,2)(c,3)] → pop → [(d,2)(b,2)]
'b' → [(d,2)(b,3)] → pop → [(d,2)]
'd' → [(d,3)] → pop → []
'a' → [(a,1)]
'a' → [(a,2)]

result: 'aa' ✅
```

## Constraints

- `1 <= s.length <= 10^5`
- `2 <= k <= 10^4`
- `s` contains only lowercase English letters

## Hints

<details>
<summary>Hint 1</summary>
A naive approach (scan → remove → repeat) works but is O(n²). Can you do it in one pass?
</details>

<details>
<summary>Hint 2</summary>
What if you stored both the character AND its current consecutive count in the stack?
</details>

<details>
<summary>Hint 3</summary>
When the top of the stack reaches count k, pop it. The characters before it automatically become adjacent again.
</details>

## Approach

Ask yourself these questions before coding:

1. What do I store in the stack — characters only, or characters + counters?
2. When do I increment the counter vs push a new entry?
3. When do I pop?
4. How do I reconstruct the final string from the stack?

## Complexity Target

| | Target |
|---|---|
| Time | O(n) |
| Space | O(n) |
