

import pytest

from random import randrange


@pytest.fixture
def make_number():
    print("I'm getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at home {number}")