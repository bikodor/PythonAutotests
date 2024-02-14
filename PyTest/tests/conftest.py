import pytest


@pytest.fixture()
def say_hello():
    print("Hello, its me")
    return 14


