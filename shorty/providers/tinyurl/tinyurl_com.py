import requests
from shorty.custom_shorty.custom import *


class tinyurlProvider:

  def tinyurl_short(url):
    response = requests.get(
      "https://tinyurl.com/api-create.php",
      dict(url = url),
      timeout = 11
    )
    if response.status_code != 200:
      return bad_request("tinyurl is not available, please try again.")
    
    return response.content.decode()