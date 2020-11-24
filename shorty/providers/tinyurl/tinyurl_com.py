import requests
from shorty.custom_shorty.custom import *
from shorty.error_msgs.errors import *


class tinyurlProvider:

  def tinyurl_short(url):
    response = requests.get(
      "https://tinyurl.com/api-create.php",
      dict(url = url),
      timeout = 11
    )
    if response.status_code != 200:
      return bad_request(tinyurl_error_msg)
    
    return response.content.decode()