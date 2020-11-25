# ~~~~~~~~~~~~~~~~~~~~~~~
HTTP_ERROR_CODE = 400 
HTTP_SUCCESS_CODE = 200 
# ~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~
VALID_URL = "https://www.youtube.com/"
INVALID_URL = "youtube.com"
EMPTY_URL = ""
INVALID_INPUT = "qwerty"
INVALID_PROTOCOL = "qwerty://www.youtube.com/"
# ~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~
VALID_PROVIDER = "tinyurl"
INVALID_PROVIDER = "tinyurll"
# ~~~~~~~~~~~~~~~~~~~~~~~

class TestShortyApi:

  def test_shorty_api_valid_url(self, post):
    """
    I) User makes request to shorten the url
    """
    response = post(
      '/shortlinks',
      data = {
        "url": VALID_URL,
        "provider": VALID_PROVIDER
      }
    )
    """
    II) Server Responds with the shorten and the original url and an HTTP success code
    """
    assert response.status_code == HTTP_SUCCESS_CODE
    assert response.get_json()['url'] is not None
    assert response.get_json()['url'] == VALID_URL
    assert response.get_json()['link'] is not None