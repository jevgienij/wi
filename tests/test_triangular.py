import pytest
import wi.triangular as tri

from typing import (
    Callable,
    List,
    Union,
)


def valid_triangular_numbers() -> List[int]:
    ret = [
        0,
        1,
        3,
        6,
        10,
        15,
        21,
    ]
    return ret


def invalid_triangular_numbers() -> List[Union[int, float]]:
    ret = [
        -1,
        -15,
        16,
        17,
        15.01,
    ]
    return ret


def check_if_triangular_functions() -> List[Callable]:
    ret = [
        tri.check_if_triangular_using_math_eq,
        tri.check_if_triangular_using_generator,
    ]
    return ret


@pytest.mark.parametrize("check_if_triangular", check_if_triangular_functions())
class TestTriangular:
    @pytest.mark.parametrize("valid_triangular_number", valid_triangular_numbers())
    def test_given_number_return_true_if_triangular(
            self, check_if_triangular, valid_triangular_number
    ):
        assert check_if_triangular(valid_triangular_number)

    @pytest.mark.parametrize("invalid_triangular_number", invalid_triangular_numbers())
    def test_given_number_return_false_if_not_triangular(
            self, check_if_triangular, invalid_triangular_number
    ):
        assert not check_if_triangular(invalid_triangular_number)
