from math import sqrt
import itertools


def check_if_triangular_using_math_eq(x: int) -> bool:
    """
    1, 3, 6, 10, 15, 21, 1 + 2 + 3 + ... + (n-1) + n

    T = (n+1)*n/2
    2*T = n^2 +n
    n^2 + n - 2*T = 0

    delta = 1 + 8T

    root = (-1 + sqrt(1 + 8T))/2

    O(1) - time complexity
    O(1) - space complexity

    :param x: number to test if it's triangular
    :return: True if given x is a triangular number
    """
    try:
        root = (-1 + sqrt(1 + 8*x))/2
    except ValueError:
        return False
    return root.is_integer()


def triangular_numbers_gen():
    """
    Generator returning triangular numbers starting from 0.
    :return: triangular numbers generator
    """
    return itertools.accumulate(itertools.count(0))


def check_if_triangular_using_generator(x: int) -> bool:
    """
    O(sqrt(x)) - time complexity
    O(1) - space complexity

    :param x: number to test if it's triangular
    :return: True if given x is a triangular number
    """
    triangular_gen = triangular_numbers_gen()
    triangular_number = next(triangular_gen)
    while True:
        if triangular_number > x:
            return False
        elif triangular_number == x:
            return True
        else:
            triangular_number = next(triangular_gen)
