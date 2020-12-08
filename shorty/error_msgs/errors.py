# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data_error_msg = {
    "Error": "[!] Request must be provided in json format.",
    "Usage": [
        {
          "url":"https://www.example.com/",
          "provider":"bitly"
        },
        {
            "url":"http://example.com/",
            "provider":"tinyurl"
        },
        {
            "url":"http://example.com"
        }
    ]
}

url_error_msg = {
    "Error": "[!] url parameter missing",
    "Usage": {
        "url":"[valid_url_here]",
        "provider":"[optional]"
    }
}

provider_error_msg = {
    "Error": "[!] The provided provider is invalid.",
    "Usage": {
        "provider":"bitly OR tinyurl"
    }
}

provided_url_error_msg = {
    "Error": "[!] The provided url is invalid.",
    "Usage": {
        "url": "https://example.com"
    }
}

get_method_error_msg = {
  "Error": "[!] The API supports only POST methods."
}

bitly_error_msg = {
  "Error": "[!] Bitly provider is unavailable for the moment.",
  "Usage": "Please use tinyurl provider or try again later."
}

tinyurl_error_msg = {
  "Error": "[!] Tinyurl provider is unavailable for the moment.",
  "Usage": "Please use bitly provider or try again later."
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~