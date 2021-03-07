import pytest

from typing import List, Union

from implementations.sort import insertion_sort, selection_sort
from utils import display as display_utils
from .conftest import TEST_LOGGER


@pytest.mark.parametrize(
    'array_data',
    [
        [-3, -2, -1, 0, 1, 2, 3],
        [6, 3, 9.9, 10, 6.1, 2, 2, 7],
        [0, 3, 8, 10, 6, -1, 2, 7],
        [3, 2, 1, 0, -1, -2, -3],
    ]
)
def test_insertion_sort(array_data: List[Union[int, float]]):

    result = insertion_sort(array=array_data, debug_logger=TEST_LOGGER)

    TEST_LOGGER.debug("Sorted array: {}".format(display_utils.format_list(result, separater="")))

    assert result == sorted(array_data)


@pytest.mark.parametrize(
    'array_data',
    [
        [-3, -2, -1, 0, 1, 2, 3],
        [6, 3, 9.9, 10, 6.1, 2, 2, 7],
        [0, 3, 8, 10, 6, -1, 2, 7],
        [3, 2, 1, 0, -1, -2, -3],
    ]
)
def test_selection_sort(array_data: List[Union[int, float]]):

    result = selection_sort(array=array_data, debug_logger=TEST_LOGGER)

    TEST_LOGGER.debug("Sorted array: {}".format(display_utils.format_list(result, separater="")))

    assert result == sorted(array_data)
