# Task: Binary Search

Implement the following Python function:

```python
def binary_search(nums: list[int], target: int) -> int:
    ...
```

## Specification

`nums` is a list of integers sorted in increasing order.

If `target` is present in `nums`, return an index `i` such that `nums[i] == target`.

If `target` is not present in `nums`, return `-1`.

If `nums` contains duplicate values, any valid index containing `target` is acceptable.

## Requirements

The function must run in time complexity $O(\log n)$.

The function must use space complexity $O(1)$.

Do not use `bisect`, `list.index`, or a linear scan.

## Examples

```python
binary_search([1, 3, 5, 7, 9], 5) == 2
binary_search([1, 3, 5, 7, 9], 2) == -1
binary_search([], 4) == -1
binary_search([10], 10) == 0
```