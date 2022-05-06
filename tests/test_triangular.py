import pytest
import wi.triangular as tri


def valid_triangular_numbers():
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


def invalid_triangular_numbers():
    ret = [
        -1,
        -15,
        16,
        17,
        15.01,
    ]
    return ret


class TestTriangular:
    @pytest.mark.parametrize("valid_triangular_number", valid_triangular_numbers())
    def test_given_number_return_true_if_triangular(self, valid_triangular_number):
        assert tri.check_if_triangular_using_math_eq(valid_triangular_number)

    @pytest.mark.parametrize("invalid_triangular_number", invalid_triangular_numbers())
    def test_given_number_return_false_if_not_triangular(self, invalid_triangular_number):
        assert not tri.check_if_triangular_using_math_eq(invalid_triangular_number)

    @pytest.mark.parametrize("valid_triangular_number", valid_triangular_numbers())
    def test_given_number_return_true_if_triangular_using_generator(self, valid_triangular_number):
        assert tri.check_if_triangular_using_generator(valid_triangular_number)

    @pytest.mark.parametrize("invalid_triangular_number", invalid_triangular_numbers())
    def test_given_number_return_false_if_not_triangular_using_generator(
            self, invalid_triangular_number
    ):
        assert not tri.check_if_triangular_using_generator(invalid_triangular_number)
