import pytest 

from shorty.providers.provider_short import *

VALID_URL = "https://www.google.com/"
VALID_PROVIDER = "bitly"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_provider_short_valid_request():
  """
  I) User provides valid request as expected
  """
  request = {
    "url": VALID_URL,
    "provider": VALID_PROVIDER
  }
  """
  II) The API's providerShort() class will take the valid request and prepare a response for the appropriate provider
  """
  response = providerShort(request).short_link()
  """
  III) After the appropriate provider shortens the link, we will get back the shortened url.
  """
  assert response['link'].startswith("https://bit.ly")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~