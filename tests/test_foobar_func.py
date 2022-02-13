from utils import foobar
import pytest


@pytest.mark.parametrize("dividend, devisor, expected_value", [(1, 1, 1.0),
                                                               (0.5, 0.5, 1.0),
                                                               ])
def test_foobar_positives(dividend, devisor, expected_value):
    assert foobar(dividend, devisor) == expected_value


@pytest.mark.parametrize("dividend, devisor, expected_exception", [(0, 0, ZeroDivisionError),
                                                                   ("1", 1, TypeError),
                                                                   (1, "1", TypeError)])
def test_foobar_exceptions(dividend, devisor, expected_exception):
    with pytest.raises(expected_exception):
        foobar(dividend, devisor)
