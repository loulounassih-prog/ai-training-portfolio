import pytest

from coding_evals.case_01_binary_search_edge_cases.model_answer import (
    binary_search,
)


def test_empty_list_returns_minus_one() -> None:
    assert binary_search([], 5) == -1


def test_middle_position_is_found() -> None:
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_absent_value_returns_minus_one() -> None:
    assert binary_search([1, 3, 5, 7, 9], 6) == -1


def test_negative_value_can_be_found() -> None:
    nums = [-10, -5, -2, 0, 4, 9]
    index = binary_search(nums, -2)
    assert index != -1
    assert nums[index] == -2


def test_duplicates_allow_any_matching_index() -> None:
    nums = [1, 2, 2, 2, 3]
    index = binary_search(nums, 2)
    assert index != -1
    assert nums[index] == 2


@pytest.mark.xfail(
    strict=True,
    reason="The exclusive loop condition skips the only candidate.",
)
def test_singleton_target_present() -> None:
    assert binary_search([10], 10) == 0


@pytest.mark.xfail(
    strict=True,
    reason="The first index can remain as an unchecked final candidate.",
)
def test_first_position_in_three_element_list() -> None:
    assert binary_search([1, 3, 5], 1) == 0


@pytest.mark.xfail(
    strict=True,
    reason="The final index remains unchecked when left equals right.",
)
def test_last_position() -> None:
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


@pytest.mark.xfail(
    strict=True,
    reason="The second element is skipped after becoming the final candidate.",
)
def test_two_element_list_second_position() -> None:
    assert binary_search([2, 8], 8) == 1