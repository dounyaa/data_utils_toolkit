from typing import TypeVar

import pytest

from data_utils_toolkit.list_utils import chunk, flatten

T = TypeVar("T")
@pytest.mark.parametrize("input, size, expected", [
    ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
    ([1, 2, 3], 5, [[1, 2, 3]]),
    ([], 3, []),
    ([1], 1, [[1]]),
])
def test_chunk(input:list[T], size:int, expected: list[list[T]]) -> None:
    assert chunk(input, size) == expected

def test_chunk_invalid_format():
    with pytest.raises(ValueError):
        chunk([1, 2, 3], 0)

def test_flatten():
    assert flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]

def test_flatten_empty():
    assert flatten([]) == []
    assert flatten([[]]) == []