# Binary Search Edge Cases — Evaluation

## Verdict

The model answer follows the general structure of binary search, but the implementation is incorrect because it can fail to inspect the final remaining candidate.

## Score

5/10

## Main Issue

The loop condition is:

```python
while left < right:
```

The implementation uses inclusive boundaries: both `left` and `right` refer to indices that may still contain the target.

When `left == right`, one valid candidate remains. However, the loop stops before checking that position.

For this implementation style, the condition should be:

```python
while left <= right:
```

## Why the Code Fails

The boundary updates are:

```python
left = mid + 1
right = mid - 1
```

These updates define a closed search interval:

```text
[left, right]
```

A closed interval is nonempty while `left <= right`.

Using `left < right` incorrectly treats the interval as empty when it contains exactly one element. The function may therefore return `-1` even when the target is present.

## Failing Edge Cases

### Single-element list

```python
binary_search([10], 10)
```

Initially, `left == right == 0`. The loop never runs, so the function incorrectly returns `-1`.

### Target at the final position

```python
binary_search([1, 3, 5, 7, 9], 9)
```

The search eventually leaves the final index as the only remaining candidate. Since `left == right`, the loop terminates before checking it.

### Two-element list

```python
binary_search([2, 8], 8)
```

After the first comparison, the second element becomes the only remaining candidate, but it is never inspected.

## What Is Correct

The answer correctly:

- uses binary search rather than a linear scan;
- computes the midpoint correctly;
- updates the search boundaries in the appropriate direction;
- returns `-1` when the target is considered absent;
- targets $O(\log n)$ time complexity and $O(1)$ auxiliary space.

However, the loop-condition error makes the implementation incorrect on important boundary cases.

## Correction Summary

The loop condition should be changed to:

```python
while left <= right:
```

This ensures that the final candidate is checked when `left == right`.

The complete corrected implementation is provided in `corrected_solution.py`.