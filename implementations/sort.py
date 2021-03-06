
from typing import List, Optional
from logging import Logger

from utils import display as display_utils


def insertion_sort(array: List[int], start: int = 0, end: Optional[int] = None, debug_logger: Optional[Logger] = None) -> List[int]:
    if debug_logger is not None:
        debug_logger.debug("Original Array: {}".format(array))

    if end is None:
        end = len(array) - 1

    for i in range(start + 1, end + 1):
        current_element = array[i]

        # Loops through the sorted sub-array,
        # shifts elements that are greater than current element to the right.
        j = i - 1
        while j >= start and array[j] > current_element:

            array[j + 1] = array[j]

            j -= 1

        array[j + 1] = current_element

        # Logs each step if debug_logger is provided.
        if debug_logger is not None:
            debug_logger.debug("Sorting Index: {:3d}. Current {:3d}. {}".format(i, current_element, display_utils.format_list(array, separater="")))

    return array
