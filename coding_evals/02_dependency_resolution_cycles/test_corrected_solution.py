from copy import deepcopy

import pytest

from coding_evals.case_02_dependency_resolution_cycles.corrected_solution import (
    resolve_dependencies,
)


def assert_topological_order(
    graph: dict[str, list[str]],
    order: list[str],
) -> None:
    assert len(order) == len(graph)
    assert set(order) == set(graph)
    positions = {node: index for index, node in enumerate(order)}

    for node, dependencies in graph.items():
        for dependency in dependencies:
            assert positions[dependency] < positions[node]


def test_empty_graph() -> None:
    assert resolve_dependencies({}) == []


def test_isolated_node() -> None:
    assert resolve_dependencies({"build": []}) == ["build"]


def test_simple_chain() -> None:
    graph = {
        "deploy": ["test"],
        "test": ["build"],
        "build": [],
    }
    assert_topological_order(graph, resolve_dependencies(graph))


def test_diamond_graph() -> None:
    graph = {
        "deploy": ["package", "test"],
        "package": ["build"],
        "test": ["build"],
        "build": [],
    }
    assert_topological_order(graph, resolve_dependencies(graph))


def test_disconnected_components() -> None:
    graph = {
        "deploy": ["build"],
        "build": [],
        "publish": ["lint"],
        "lint": [],
    }
    assert_topological_order(graph, resolve_dependencies(graph))


def test_two_node_cycle() -> None:
    graph = {"a": ["b"], "b": ["a"]}
    with pytest.raises(ValueError, match="Dependency cycle detected"):
        resolve_dependencies(graph)


def test_long_cycle() -> None:
    graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
    with pytest.raises(ValueError, match="a -> b -> c -> a"):
        resolve_dependencies(graph)


def test_self_cycle() -> None:
    with pytest.raises(ValueError, match="a -> a"):
        resolve_dependencies({"a": ["a"]})


def test_unknown_dependency() -> None:
    graph = {"deploy": ["missing"]}
    with pytest.raises(
        KeyError,
        match="Unknown dependency 'missing' referenced by 'deploy'",
    ):
        resolve_dependencies(graph)


def test_input_is_not_mutated() -> None:
    graph = {
        "deploy": ["test"],
        "test": ["build"],
        "build": [],
    }
    original = deepcopy(graph)
    resolve_dependencies(graph)
    assert graph == original