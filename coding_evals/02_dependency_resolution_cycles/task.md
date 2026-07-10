# Dependency Resolution and Cycle Detection — Task

Implement the following function:

```python
def resolve_dependencies(
    graph: dict[str, list[str]],
) -> list[str]:
    raise NotImplementedError("Implement according to the specification.")
```

The dictionary maps each task or package to its direct dependencies. Every dependency must appear before the task that depends on it in the returned list.

Example:

```python
graph = {
    "deploy": ["test"],
    "test": ["build"],
    "build": [],
}
```

A valid result is:

```python
["build", "test", "deploy"]
```

Requirements:

- every dependency must also be a key in `graph`;
- an unknown dependency must raise a clear `KeyError`;
- a dependency cycle must raise a clear `ValueError`;
- the input graph must not be modified;
- any valid topological order is acceptable;
- the expected complexity is $O(V+E)$;
- no external library is required.