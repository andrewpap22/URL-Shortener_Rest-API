from shorty.providers.bitly.bit_ly import *

VALID_URL = "https://www.google.com/"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_bitly_provider():
  """
  I) Pass a valid url to the provider
  """
  res = bitlyProvider.bitly_short(VALID_URL)
  """
  II) Check the result
  """
  assert res.startswith('https://bit.ly/')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~