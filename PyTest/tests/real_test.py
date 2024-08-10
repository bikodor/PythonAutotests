import requests
from PyTest.src.baseclasses.response_pydantic import Response
from PyTest.configuration import SERVICE_URL_2
from PyTest.src.pydantic_schemas.user import User


# resp = requests.get(SERVICE_URL_2)

def test_getting_users_list():

    response = requests.get(SERVICE_URL_2)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.validate(User)