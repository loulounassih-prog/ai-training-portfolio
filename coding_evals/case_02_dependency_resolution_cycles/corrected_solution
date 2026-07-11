def resolve_dependencies(
    graph: dict[str, list[str]],
) -> list[str]:
    """Return a topological order or raise for invalid dependency graphs."""
    for node, dependencies in graph.items():
        for dependency in dependencies:
            if dependency not in graph:
                raise KeyError(
                    f"Unknown dependency {dependency!r} referenced by {node!r}."
                )

    unvisited = 0
    visiting = 1
    visited = 2
    state = {node: unvisited for node in graph}
    path: list[str] = []
    order: list[str] = []

    def visit(node: str) -> None:
        if state[node] == visited:
            return
        if state[node] == visiting:
            cycle_start = path.index(node)
            cycle = path[cycle_start:] + [node]
            cycle_text = " -> ".join(cycle)
            raise ValueError(f"Dependency cycle detected: {cycle_text}")

        state[node] = visiting
        path.append(node)

        for dependency in graph[node]:
            visit(dependency)

        path.pop()
        state[node] = visited
        order.append(node)

    for node in graph:
        if state[node] == unvisited:
            visit(node)

    return order