# Dependency Resolution and Cycle Detection — Rubric

**Total: 10 points**

| Criterion | Maximum |
|---|---:|
| Valid ordering for acyclic graphs | 3 |
| Cycle detection | 3 |
| Unknown-dependency validation | 1 |
| Input preservation and interface | 1 |
| Complexity and code quality | 2 |
| **Total** | **10** |

## 1. Valid Ordering for Acyclic Graphs — 3 Points

- **3 points:** Returns every graph key exactly once and places every dependency before its dependent for empty, connected, diamond, and disconnected DAGs.
- **2 points:** Works for simple DAGs but misses a meaningful acyclic structure.
- **1 point:** Produces partially useful orders with substantial omissions or duplication.
- **0 points:** Does not implement dependency ordering.

## 2. Cycle Detection — 3 Points

- **3 points:** Detects self-cycles and cycles of arbitrary length and raises a clear `ValueError`.
- **2 points:** Detects most cycles but misses one required form or provides an unclear failure mode.
- **1 point:** Attempts cycle detection but confuses active and completed nodes.
- **0 points:** Silently accepts cycles.

## 3. Unknown-Dependency Validation — 1 Point

- **1 point:** Raises a clear `KeyError` when any referenced dependency is absent from the graph keys.
- **0 points:** Ignores, inserts, or otherwise silently accepts unknown dependencies.

## 4. Input Preservation and Interface — 1 Point

- **1 point:** Preserves the input and follows the required typed function signature.
- **0 points:** Mutates the graph or violates the interface.

## 5. Complexity and Code Quality — 2 Points

- **2 points:** Runs in $O(V+E)$ time, uses appropriate state, and is readable and documented without unnecessary abstraction.
- **1 point:** Has the intended asymptotic traversal but contains a material state-model or clarity defect.
- **0 points:** Has avoidable superlinear traversal on valid inputs or is materially unreliable.

Any topologically valid output order receives full credit. Kahn's algorithm, a three-state DFS, or another rigorous $O(V+E)$ method is acceptable; the response need not match the reference implementation.