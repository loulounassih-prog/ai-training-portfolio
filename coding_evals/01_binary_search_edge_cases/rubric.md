# Binary Search Edge Cases — Rubric

**Total: 10 points**

| Criterion | Maximum |
|---|---:|
| Genuine binary-search approach | 2 |
| Consistent interval invariant and updates | 3 |
| Correct return behavior | 2 |
| Required edge-case handling | 2 |
| Complexity and code quality | 1 |
| **Total** | **10** |

## 1. Genuine Binary-Search Approach — 2 Points

- **2 points:** Uses ordered comparisons and repeatedly reduces the candidate interval by approximately half.
- **1 point:** Attempts binary search but contains structural mistakes that prevent reliable interval reduction.
- **0 points:** Uses a linear scan, `list.index`, `bisect`, or another prohibited approach.

## 2. Consistent Interval Invariant and Updates — 3 Points

- **3 points:** Uses a consistent inclusive or half-open interval invariant, a compatible loop condition, and updates that guarantee progress without discarding possible matches.
- **2 points:** The invariant is mostly correct but contains a minor boundary omission.
- **1 point:** The midpoint and update directions are reasonable, but the loop condition is incompatible with the stated bounds.
- **0 points:** The updates can loop indefinitely or discard arbitrary valid regions.

## 3. Correct Return Behavior — 2 Points

- **2 points:** Returns an index containing the target whenever present and `-1` whenever absent. Any matching index is accepted for duplicates.
- **1 point:** Works on ordinary cases but fails on a meaningful subset of valid inputs.
- **0 points:** Frequently returns incorrect values or violates the required interface.

## 4. Required Edge-Case Handling — 2 Points

- **2 points:** Correctly handles empty lists, singletons, first and last positions, absent values, duplicates, negative numbers, and small lists.
- **1 point:** Misses only a narrow edge case.
- **0 points:** Fails multiple required boundary cases or all single-candidate states.

## 5. Complexity and Code Quality — 1 Point

- **1 point:** Runs in $O(\log n)$ time with $O(1)$ auxiliary space and is readable, typed, and compatible with Python 3.11+.
- **0 points:** Violates the complexity requirements or is materially unclear.

Equivalent correct binary-search formulations, including half-open interval implementations, receive full credit. The task does not ask the model to write tests, so no rubric points are assigned for test coverage.