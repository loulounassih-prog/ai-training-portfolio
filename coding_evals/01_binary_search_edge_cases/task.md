# Binary Search Edge Cases — Task

Implement the following function:

```python
def binary_search(nums: list[int], target: int) -> int:
    raise NotImplementedError("Implement according to the specification.")
```

`nums` is a list of integers sorted in nondecreasing order. If `target` is present, return any index `i` such that `nums[i] == target`. If `target` is absent, return `-1`.

The implementation must:

- run in $O(\log n)$ time;
- use $O(1)$ auxiliary space;
- support empty lists, duplicate values, and negative integers;
- avoid `bisect`, `list.index`, and linear scans.

Examples:

```python
binary_search([1, 3, 5, 7, 9], 5) == 2
binary_search([1, 3, 5, 7, 9], 2) == -1
binary_search([], 4) == -1
binary_search([10], 10) == 0
```