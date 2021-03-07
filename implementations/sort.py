
from typing import List, Optional, Union
from logging import Logger

from utils import display as display_utils
from utils import time_usage as time_utils


@time_utils.log_time_usage()
def insertion_sort(array: List[Union[int, float]], start: int = 0, end: Optional[int] = None, debug_logger: Optional[Logger] = None) -> List[Union[int, float]]:
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

        # Inserts current element to the emptied space.
        array[j + 1] = current_element

    # Logs sorted array
    if debug_logger is not None:
        debug_logger.debug("Sorted array: {}".format(display_utils.format_list(array=array, separater="")))

    return array


@time_utils.log_time_usage()
def selection_sort(array: List[Union[int, float]], start: int = 0, end: Optional[int] = None, debug_logger: Optional[Logger] = None) -> List[Union[int, float]]:
    if debug_logger is not None:
        debug_logger.debug("Original Array: {}".format(array))

    if end is None:
        end = len(array) - 1

    # Loops from start to end - 1 of the array.
    for i in range(start, end):
        current_element = array[i]

        # Loops from current index + 1 to end,
        # finds the smallest element and exchange it with current element.
        min_element_index = i
        for j in range(i + 1, end + 1):
            if array[j] < array[min_element_index]:
                min_element_index = j

        array[i] = array[min_element_index]
        array[min_element_index] = current_element

        # Logs each step if debug_logger is provided.
        if debug_logger is not None:
            debug_logger.debug("Sorting Index: {:3}. Current {:3}. {}".format(i, current_element, display_utils.format_list(array, separater="")))

    # Logs sorted array
    if debug_logger is not None:
        debug_logger.debug("Sorted array: {}".format(display_utils.format_list(array=array, separater="")))

    return array
