def resolve_dependencies(
    graph: dict[str, list[str]],
) -> list[str]:
    visited: set[str] = set()
    order: list[str] = []

    def visit(node: str) -> None:
        if node in visited:
            return

        visited.add(node)
        for dependency in graph.get(node, []):
            visit(dependency)
        order.append(node)

    for node in graph:
        visit(node)

    return order