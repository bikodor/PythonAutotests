from PyTest.src.pydantic_schemas.post import Post
import requests
from PyTest.configuration import SERVICE_URL
from PyTest.src.baseclasses.response_pydantic import Response



def test_get_request():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.validate(Post)
    response.assert_status_code(200)
    response.assert_element_count()

