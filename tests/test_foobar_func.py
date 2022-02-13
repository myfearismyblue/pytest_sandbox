from utils import foobar
import pytest

@pytest.mark.parametrize("dividend, deviser, expected_value", [(1, 1, 1.0),
                                                               (0.5, 0.5, 1.0),
                                                               ])
def test_foobar_positives(dividend, deviser, expected_value):
    assert foobar(dividend, deviser) == expected_value
