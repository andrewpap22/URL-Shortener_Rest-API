from shorty.providers.tinyurl.tinyurl_com import *

VALID_URL = "https://www.google.com/"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_tinyurl_com_provider():
  """
  I) Pass a valid url to the provider
  """
  res = tinyurlProvider.tinyurl_short(VALID_URL)
  """
  II) Check the result
  """
  assert res.startswith('https://tinyurl.com/')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~