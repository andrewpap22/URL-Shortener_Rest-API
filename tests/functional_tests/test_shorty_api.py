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

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def test_shorty_api_invalid_url(self, post):
    """
    I) User makes request to shorten url, but provides invalid url
    """
    response = post(
      '/shortlinks',
      data = {
        "url": INVALID_URL
      }
    )
    """
    II) Server responds with an HTTP error status code,
    and provides a usefull error message.
    """
    assert response.status_code == HTTP_ERROR_CODE
    assert response.get_json() == {
      "message": {
        "Error": "[!] The provided url is invalid.",
        "Usage": {
            "url": "https://example.com"
        }
      }
    }
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def test_shorty_api_invalid_input(self, post):
    """
    I) User makes request to shorten url, but provides anything but a url.
    """
    response = post(
      '/shortlinks',
      data = {
        "url": INVALID_INPUT
      }
    )
    """
    II) Server responds with an HTTP error status code,
    and provides a usefull error message.
    """
    assert response.status_code == HTTP_ERROR_CODE
    assert response.get_json() == {
      "message": {
        "Error": "[!] The provided url is invalid.",
        "Usage": {
            "url": "https://example.com"
        }
      }
    }
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def test_shorty_api_empty_url(self, post):
    """
    I) User makes request to shorten url, but does not provide url.
    """
    response = post(
      '/shortlinks',
      data = {
        "url": EMPTY_URL
      }
    )
    """
    II) Server responds with an HTTP error status code,
    and provides a usefull error message.
    """
    assert response.status_code == HTTP_ERROR_CODE
    assert response.get_json() == {
      "message": {
        "Error": "[!] The provided url is invalid.",
        "Usage": {
            "url": "https://example.com"
        }
      }
    }
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def test_shorty_api_invalid_url_protocol(self, post):
    """
    I) User makes request to shorten url, but provides any protocol other than http or https.
    """
    response = post(
      '/shortlinks',
      data = {
        "url": INVALID_PROTOCOL
      }
    )
    """
    II) Server responds with an HTTP error status code,
    and provides a usefull error message.
    """
    assert response.status_code == HTTP_ERROR_CODE
    assert response.get_json() == {
      "message": {
        "Error": "[!] The provided url is invalid.",
        "Usage": {
            "url": "https://example.com"
        }
      }
    }
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def test_shorty_api_invalid_provider(self, post):
    """
    I) User chooses the provider afterall, but provides invalid provider in the request.
    """
    response = post(
      '/shortlinks',
      data = {
        "url": VALID_URL,
        "provider": INVALID_PROVIDER
      }
    )
    """
    II) The server responds with an bad request HTTP status code and provides a useful usage message.
    """
    assert response.status_code == HTTP_ERROR_CODE
    assert response.get_json() == {
      "message": {
        "Error": "[!] The provided provider is invalid.",
        "Usage": {
            "provider": "bitly OR tinyurl"
        }
      }
    }
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def test_shorty_api_no_data_provided(self, post):
    """
    I) User does not provide any data at all in his/her request
    """
    response = post(
      '/shortlinks',
      data = {}
    )
    """
    II) The server responds with an HTTP error status code and an appropriate message for the user.
    """
    assert response.status_code == HTTP_ERROR_CODE
    assert response.get_json() == {
      "message": {
        "Error": "[!] Request must be provided in json format."
      }
    }
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~