import pytest
from PyTest.src.generators.json_player import Json_Player
from PyTest.src.generators.player_localization import PlayerLocalization

@pytest.mark.parametrize("status", [
    "active",
    "inactive"

])
def test_player_validate(status, get_player_generator):
    response = get_player_generator.set_status(status).build()
    assert Json_Player.model_validate(response)

@pytest.mark.parametrize("balance", [
    20,
    500,

])
def test_player_balance_validation(balance, get_player_generator):
    response = get_player_generator.set_balance(balance).build()
    assert Json_Player.model_validate(response)

def test_player_france(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        'localize', PlayerLocalization('fr_FR').build()
    ).build()
    print(object_to_send)

def test_create_new_json(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        ["localize", "fr", "is", "the", "best", "lang"], PlayerLocalization("fr_FR").build()
    ).build()
    print(object_to_send)