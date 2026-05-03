# Search Insert Position

## Problem

Given a sorted array of distinct integers and a target value, return the index where the target is found. If the target is not found, return the index where it **would be inserted** to keep the array sorted.

## Examples

```
search_insert([1, 3, 5, 6], 5)  → 2
search_insert([1, 3, 5, 6], 2)  → 1
search_insert([1, 3, 5, 6], 7)  → 4
search_insert([1, 3, 5, 6], 0)  → 0
```

## Constraints

- All integers in `nums` are distinct
- `nums` is sorted in ascending order
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i], target <= 10^4`

## Hints

<details>
<summary>Hint 1</summary>

C'est une recherche binaire classique — mais que retournes-tu quand `target` n'est **pas** trouvé ?

</details>

<details>
<summary>Hint 2</summary>

Observe la valeur de `left` quand la boucle se termine sans avoir trouvé `target`. Que représente-t-elle par rapport au tableau ?

</details>

<details>
<summary>Hint 3</summary>

À la sortie de la boucle, `left` pointe toujours vers le premier élément **strictement supérieur** à `target` — c'est exactement l'index d'insertion. Retourne `left`.

</details>

## Approach

Pose-toi ces questions avant de coder :

1. Quelle est la différence avec une recherche binaire classique ?
2. Que vaut `left` quand la boucle se termine sans trouver `target` ?
3. Est-ce que tu as besoin d'un cas spécial pour l'insertion, ou `left` suffit ?

## Edge Cases

| Cas | Entrée | Résultat attendu |
|---|---|---|
| Target trouvé | `[1, 3, 5, 6], 5` | `2` |
| Target plus petit que tout | `[1, 3, 5, 6], 0` | `0` |
| Target plus grand que tout | `[1, 3, 5, 6], 7` | `4` |
| Target entre deux éléments | `[1, 3, 5, 6], 2` | `1` |
| Tableau à un élément | `[1], 0` | `0` |

## Complexity Target

| | Target |
|---|---|
| Time | O(log n) |
| Space | O(1) |

## Solution

<details>
<summary>Solution</summary>

```python
def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # left est l'index d'insertion quand target n'est pas trouvé
    return left
```

</details>