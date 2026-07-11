from copy import deepcopy

import pytest

from coding_evals.case_02_dependency_resolution_cycles.model_answer import (
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


def test_input_is_not_mutated() -> None:
    graph = {
        "deploy": ["test"],
        "test": [],
    }
    original = deepcopy(graph)
    resolve_dependencies(graph)
    assert graph == original


@pytest.mark.xfail(
    strict=True,
    reason="A single visited set cannot distinguish a recursion-stack node.",
)
def test_two_node_cycle_raises_value_error() -> None:
    graph = {"a": ["b"], "b": ["a"]}
    with pytest.raises(ValueError, match="cycle"):
        resolve_dependencies(graph)


@pytest.mark.xfail(
    strict=True,
    reason="The implementation silently accepts cycles longer than two.",
)
def test_long_cycle_raises_value_error() -> None:
    graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
    with pytest.raises(ValueError, match="cycle"):
        resolve_dependencies(graph)


@pytest.mark.xfail(
    strict=True,
    reason="A self-cycle is treated as an already visited node.",
)
def test_self_cycle_raises_value_error() -> None:
    with pytest.raises(ValueError, match="cycle"):
        resolve_dependencies({"a": ["a"]})


@pytest.mark.xfail(
    strict=True,
    reason="graph.get silently converts an unknown dependency into a leaf.",
)
def test_unknown_dependency_raises_key_error() -> None:
    graph = {"deploy": ["missing"]}
    with pytest.raises(KeyError, match="Unknown dependency"):
        resolve_dependencies(graph)