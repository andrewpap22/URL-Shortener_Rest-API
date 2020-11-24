import requests
import json

from shorty.custom_shorty.custom import *
from shorty.error_msgs.errors import *


class bitlyProvider:

  def bitly_short(url):

    bitly_header = {'Authorization':'4a410e924ad26bf27281e7a46ea128028ce46404', 'Content-Type':'application/json'}

    # get the group UID associated with our account
    groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=bitly_header)

    if groups_res.status_code == 200:
      # if response is OK, get the GUID
      groups_data = groups_res.json()['groups'][0]
      guid = groups_data['guid']
    else:
      print("[!] Cannot get GUID...")

    bitly_data = {
        "long_url": url,
        "group_guid": guid
    }

    short_link_resp = requests.post('https://api-ssl.bitly.com/v4/shorten',json=bitly_data, headers=bitly_header)
    
    if short_link_resp.status_code != 200:
      return bad_request(bitly_error_msg)

    short_link_json = short_link_resp.json()
    short_link = short_link_json["link"]
    return short_link
    
