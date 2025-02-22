from typing import Callable, Iterable, Iterator


def ft_filter(filter_func: Callable, iterable: Iterable) -> Iterator:
    """
    Return an iterator yielding those items of iterable for which function(item) is true. 
    If function is None, return the items that are true.
    """
    return (iter for iter in iterable if filter_func(iter))


def is_even(num: int) -> bool:
    return num % 2 == 0


def main():
    try:
        numbers = [1, 2, 3, 4, 5, 6]
        print(list(ft_filter(is_even, numbers)))
        print(list(filter(is_even, numbers)))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
