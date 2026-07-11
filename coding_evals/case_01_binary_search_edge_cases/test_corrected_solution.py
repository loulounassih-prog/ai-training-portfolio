import pytest

from coding_evals.case_01_binary_search_edge_cases.corrected_solution import (
    binary_search,
)


def assert_found(nums: list[int], target: int) -> None:
    index = binary_search(nums, target)
    assert index != -1
    assert nums[index] == target


def test_empty_list() -> None:
    assert binary_search([], 5) == -1


def test_singleton_target_present() -> None:
    assert binary_search([10], 10) == 0


def test_singleton_target_absent() -> None:
    assert binary_search([10], 3) == -1


def test_target_at_first_position() -> None:
    assert binary_search([1, 3, 5], 1) == 0


def test_target_in_middle() -> None:
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_target_at_last_position() -> None:
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


@pytest.mark.parametrize("target", [6, -4, 12])
def test_absent_values(target: int) -> None:
    assert binary_search([1, 3, 5, 7, 9], target) == -1


def test_two_element_lists() -> None:
    assert binary_search([2, 8], 2) == 0
    assert binary_search([2, 8], 8) == 1
    assert binary_search([2, 8], 5) == -1


def test_negative_numbers() -> None:
    assert_found([-10, -5, -2, 0, 4, 9], -5)


@pytest.mark.parametrize(
    ("nums", "target"),
    [
        ([1, 2, 2, 2, 3], 2),
        ([4, 4, 4, 4], 4),
        ([-3, -3, -1, 0, 2], -3),
    ],
)
def test_duplicates_return_valid_matching_index(
    nums: list[int],
    target: int,
) -> None:
    assert_found(nums, target)