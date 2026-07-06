# Evaluation

## Verdict

The submitted answer contains the general idea of binary search, but it is not fully correct.

## Score

5/10

## What is correct

The solution uses the standard binary search structure with `left`, `right`, and `mid`.

The intended time complexity is $O(\log n)$, and the space complexity is $O(1)$.

The boundary updates are close to a correct implementation:

```python
left = mid + 1
right = mid - 1
```

These updates are appropriate for a binary search that discards the already-tested midpoint.

## Main issue

The loop condition is incorrect for this implementation:

```python
while left < right:
```

With this condition, the loop stops as soon as `left == right`. However, when `left == right`, there is still one remaining candidate index that has not necessarily been checked.

As a result, the last possible candidate is never tested.

## Failing edge cases

This bug breaks simple cases such as:

```python
binary_search([10], 10)
```

Expected result: `0`

Actual result: `-1`

It also fails when the target is the last remaining candidate:

```python
binary_search([1, 3], 3)
binary_search([1, 3, 5, 7], 7)
```

In these cases, the search narrows down to the final index, but the loop exits before checking it.

## Correction summary

For this style of binary search, where `right` is an inclusive boundary and the midpoint is discarded with `mid + 1` or `mid - 1`, the loop should be:

```python
while left <= right:
```

This ensures that the final candidate is checked before returning `-1`.