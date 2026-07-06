import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("corrected_solution.py")
SPEC = importlib.util.spec_from_file_location(
    "binary_search_corrected_solution",
    MODULE_PATH,
)

assert SPEC is not None
assert SPEC.loader is not None

module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

binary_search = module.binary_search


def test_empty_list() -> None:
    assert binary_search([], 5) == -1


def test_single_element_target_present() -> None:
    assert binary_search([10], 10) == 0


def test_single_element_target_absent() -> None:
    assert binary_search([10], 3) == -1


def test_target_at_beginning() -> None:
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 1) == 0


def test_target_in_middle() -> None:
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 5) == 2


def test_target_at_end() -> None:
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 9) == 4


def test_target_absent_between_values() -> None:
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 6) == -1


def test_target_less_than_minimum() -> None:
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, -4) == -1


def test_target_greater_than_maximum() -> None:
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 12) == -1


def test_two_elements_target_in_second_position() -> None:
    nums = [2, 8]
    assert binary_search(nums, 8) == 1


def test_negative_numbers() -> None:
    nums = [-10, -5, -2, 0, 4, 9]
    assert binary_search(nums, -5) == 1


@pytest.mark.parametrize(
    ("nums", "target"),
    [
        ([1, 2, 2, 2, 3], 2),
        ([4, 4, 4, 4], 4),
        ([-3, -3, -1, 0, 2], -3),
    ],
)
def test_duplicates_return_valid_matching_index(nums: list[int], target: int) -> None:
    index = binary_search(nums, target)

    assert index != -1
    assert nums[index] == target