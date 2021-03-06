from typing import List
import pytest

from implementations.sort import insertion_sort
from utils import display as display_utils
from .conftest import TEST_LOGGER


@pytest.mark.parametrize(
    'array_data',
    [
        [1, 3, 8, 10, 6, 2, 2, 7],
        [6, 3, 99, 10, 6, 2, 2, 7],
        [0, 3, 8, 10, 6, -1, 2, 7],
        [1, 3, 8, -10, -2, 2, 2, 7],
    ]
)
def test_insertion_sort(array_data: List[int]):

    result = insertion_sort(array=array_data, debug_logger=TEST_LOGGER)

    TEST_LOGGER.debug("Sorted array: {}".format(display_utils.format_list(result, separater="")))

    assert result == sorted(array_data)
