from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    first = 0
    last = len(numbers) - 1

    while first <= last:
        middle = int((first + last) / 2)
        if numbers[middle] == value:
            return True, 1
        if numbers[middle] < value:
            first += 1
        else:
            last -= 1
        
    return False, -1


ints = array('I', [1, 5, 6, 7, 10, 26, 29, 40])

print(binary_search(ints, 7))
