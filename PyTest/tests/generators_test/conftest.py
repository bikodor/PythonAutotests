import pytest
from PyTest.src.generators.player import Player

@pytest.fixture
def get_player_generator():
    return Player()