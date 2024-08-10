import pytest

@pytest.mark.development
def test_dev():
    assert 1 == 1, 'Not equal'


@pytest.mark.testing
def test_test():
    assert 2 == 2, "Not equal"


@pytest.mark.production
def test_prod():
    assert 3 == 3, "Not equal"


@pytest.mark.development
@pytest.mark.testing
def test_for_dev_and_test():
    assert 4 == 4, "Not equal"