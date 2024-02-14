import pytest

@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (5, 2, 7),
    (-1, 6, 5),
])
def test_positive_number(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) >= 0, "This Number not positive"