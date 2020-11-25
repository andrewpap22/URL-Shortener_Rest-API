from shorty.custom_shorty.custom import *

VALID_URL = "https://www.google.com/"

LONG_LONG_URL = "https://www.google.com/search?sxsrf=ALeKk01JjGA_6Q04PsNvryb_0l9huxt0sA%3A1606314212324&source=hp&ei=5Gi-X4yaEJKTjLsPrvSQmAE&q=qewrty&oq=qewrty&gs_lcp=CgZwc3ktYWIQAzIHCAAQyQMQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoECCMQJzoCCC46AggAOggILhDHARCjAjoICC4QyQMQkQI6BQgAEJECOgQIABBDOgQILhBDOgsILhDJAxCRAhCTAjoHCCMQ6gIQJzoHCC4Q6gIQJzoICAAQyQMQkQI6BwgjELECECc6BwgAEMkDEENKBQg8EgEyUOYMWMsZYP4aaANwAHgBgAHQAogBlw6SAQcwLjIuMy4ymAEAoAEBqgEHZ3dzLXdperABCg&sclient=psy-ab&ved=0ahUKEwiMnJTg8p3tAhWSCWMBHS46BBMQ4dUDCAc&uact=5"

URL_WITHOUT_HTTP = "www.example.com"
INVALID_URL = "qwerty"
URL_INVALID_PROTOCOL = "qwerty://www.google.com/"

VALID_PROVIDER = "tinyurl"
NON_VALID_PROVIDER = "qwerty"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_url_valid():
  """
  I) Pass a valid url to the function.
  """
  res = url_valid(VALID_URL)
  """
  II) Check the result
  """
  assert res
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_url_valid_long():
  """
  I) Pass the long url with multiple parameteres to the function for validation
  """
  res = url_valid(LONG_LONG_URL)
  """
  II) The function should accept that link as well.
  """
  assert res
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_url_without_HTTP():
  """
  I) Pass a url to the function without http or https protocol
  """
  res = url_valid(URL_WITHOUT_HTTP)
  """
  II) Check the result
      Keep in mind that assert checks if something is true, and if it's not then it triggers an assertion error. 
      That's the reason we add the not keyword in this particular case.
  """
  assert not res
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_url_invalid():
  """
  I) Pass an invalid url to the function.
  """
  res = url_valid(INVALID_URL)
  """
  II) Check the result
  """
  assert not res
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_url_invalid_protocol():
  """
  I) Pass a url with invalid protocol to the function.
  """
  res = url_valid(URL_INVALID_PROTOCOL)
  """
  II) Check the result
  """
  assert not res
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_provider_valid_justifiable_provider():
  """
  I) Pass the valid provider to the function
  """
  res = provider_valid(VALID_PROVIDER)
  """
  II) Check the result
  """
  assert res
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_provider_valid_non_justifiable_provider():
  """
  I) Pass the non valid provider to the function
  """
  res = provider_valid(NON_VALID_PROVIDER)
  """
  II) Check the result
  """
  assert not res
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
From this point and on we're going to test the custom shorten() function for a given valid url.
"""
def test_shorten():
  """
  I) Provide a valid url
  """
  res = shorten(VALID_URL)
  """
  II) Check the result
  """
  assert res.startswith('http://')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~