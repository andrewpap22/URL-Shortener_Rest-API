from shorty.providers.bitly.bit_ly import *
from shorty.providers.tinyurl.tinyurl_com import *
from shorty.custom_shorty.custom import *

class providerShort:
  """Class for shortening a url requested   by the user using the providers requested. If none provider is requested then the url will be  shorted using the default tinyurl provider. Also if both tinyurl, bitly are unavailable for any reason, user will be informed with a message that the providers are unavailable and the link will be shortened with a customly created short function. 
    Parameters:
    The user request (url and provider(optional))
    Return values:
    Returning the request to the appropriate provider.
    """
  DEFAULT = "bitly"

  def __init__(self, request):
    provider = self.get_provider(request)

    # making sure the provider string is in correct format.
    self.provider = provider.lower()
    
    self.url = request['url']
    self.link = ""
  
  def get_provider(self, request):
    if 'provider' not in request:
      return self.DEFAULT
    return request['provider']

  def short_link(self):

    # step 1: shorten the url with the provider selected 
    if self.provider == 'tinyurl':
      self.link = tinyurlProvider.tinyurl_short(self.url)
    elif self.provider == 'bitly':
      self.link = bitlyProvider.bitly_short(self.url)
    else:
      self.link = shorten(self.url)

    # step 2: return the shorted url.
    return self.send_response()

  def send_response(self):
    final_response = {
      "url": self.url,
      "link": self.link,
    }
    return final_response
