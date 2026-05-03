# First and Last Position

## Problem

Given a sorted array of integers (which may contain duplicates) and a target value, return the **first and last position** of the target in the array.

If the target is not found, return `[-1, -1]`.

## Examples

```
find_first_last([5, 7, 7, 8, 8, 10], 8)  → [3, 4]
find_first_last([5, 7, 7, 8, 8, 10], 6)  → [-1, -1]
find_first_last([1, 1, 1, 1], 1)          → [0, 3]
find_first_last([], 0)                    → [-1, -1]
```

## Constraints

- The array is sorted in ascending order
- The array may contain duplicates
- The array can be empty → return `[-1, -1]`
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`

## Hints

<details>
<summary>Hint 1</summary>

La recherche binaire classique s'arrête dès qu'elle trouve `target`. Mais ici tu veux le **premier** et le **dernier**. Que se passe-t-il si tu continues à chercher après avoir trouvé ?

</details>

<details>
<summary>Hint 2</summary>

Quand `nums[mid] == target`, au lieu de retourner immédiatement, **mémorise** la position puis continue à chercher dans une direction. Laquelle selon que tu cherches le bord gauche ou droit ?

</details>

<details>
<summary>Hint 3</summary>

Fais deux passes binaires séparées avec un paramètre `left: bool` :
- Bord gauche : quand `nums[mid] == target` → mémorise et continue à **gauche** (`hi = mid - 1`)
- Bord droit : quand `nums[mid] == target` → mémorise et continue à **droite** (`lo = mid + 1`)

</details>

## Approach

Pose-toi ces questions avant de coder :

1. Pourquoi une seule recherche binaire ne suffit-elle pas ?
2. Que se passe-t-il quand `nums[mid] == target` dans chaque passe ?
3. Que retournes-tu si `target` n'est jamais trouvé ?
4. Peux-tu factoriser les deux passes en une seule fonction avec un paramètre ?

## Edge Cases

| Cas | Entrée | Résultat attendu |
|---|---|---|
| Tableau vide | `[], 0` | `[-1, -1]` |
| Tous identiques | `[1, 1, 1, 1], 1` | `[0, 3]` |
| Un seul élément trouvé | `[5], 5` | `[0, 0]` |
| Un seul élément non trouvé | `[5], 3` | `[-1, -1]` |
| Target absent | `[1, 2, 3], 4` | `[-1, -1]` |
| Target en début | `[8, 8, 9, 10], 8` | `[0, 1]` |
| Target en fin | `[1, 2, 8, 8], 8` | `[2, 3]` |

## Complexity Target

| | Target |
|---|---|
| Time | O(log n) |
| Space | O(1) |

## Solution

<details>
<summary>Solution</summary>

```python
def find_first_last(nums: list[int], target: int) -> list[int]:
    return [find_bound(nums, target, left=True),
            find_bound(nums, target, left=False)]


def find_bound(nums: list[int], target: int, left: bool) -> int:
    lo, hi = 0, len(nums) - 1
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            result = mid
            if left:
                hi = mid - 1  # continue à gauche → cherche une occurrence plus tôt
            else:
                lo = mid + 1  # continue à droite → cherche une occurrence plus tard
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return result
```

</details>