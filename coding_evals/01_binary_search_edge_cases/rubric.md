# Rubric

Total: 10 points

## 1. Correct binary search logic: 2 points

The solution must implement a genuine binary search over a sorted list.

Full credit requires maintaining search boundaries, computing a midpoint, and reducing the search interval at each step.

No credit should be given for linear scans or use of prohibited helpers such as `list.index`.

## 2. Loop condition and boundary updates: 2 points

The implementation must use a loop condition and boundary updates that correctly handle all remaining candidates.

For an inclusive `right` boundary, a correct loop condition is:

```python
while left <= right:
```

The updates should discard the tested midpoint correctly:

```python
left = mid + 1
right = mid - 1
```

Solutions that skip the final candidate should lose significant credit.

## 3. Correct return values: 1.5 points

The function must return an index where `nums[index] == target` when the target is present.

The function must return `-1` when the target is absent.

For duplicate values, any valid matching index is acceptable.

## 4. Edge case handling: 1.5 points

The solution should correctly handle:

- empty lists;
- one-element lists;
- two-element lists;
- target at the first index;
- target at the last index;
- target absent but within the value range;
- target below the minimum value;
- target above the maximum value;
- negative numbers;
- duplicate values.

## 5. Complexity: 1 point

The solution must run in time complexity $O(\log n)$.

The solution must use space complexity $O(1)$.

## 6. Code clarity and type compatibility: 1 point

The code should be simple, readable, idiomatic Python 3.10+, and compatible with the required function signature:

```python
def binary_search(nums: list[int], target: int) -> int:
    ...
```

## 7. Test coverage: 1 point

The tests should cover normal cases and important edge cases.

They should specifically catch boundary bugs such as failing to test the final remaining candidate.