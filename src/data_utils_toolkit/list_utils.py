from typing import TypeVar

T = TypeVar("T")

def chunk(items: list[T], size: int) -> list[list[T]]:
    """Break a list into chunks of size N"""
    if size <=0 :
        raise ValueError("size must be a positive integer")
    
    return [items[i : i+size] for i in range(0, len(items), size)]

def flatten(nested: list[list[T]]) -> list[T]:
    """turning a nested list structure into a single flat list"""
    return [item for element in nested for item in element]