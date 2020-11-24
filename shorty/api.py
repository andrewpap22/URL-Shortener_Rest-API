from shorty.providers.provider_short import *

api = Blueprint('api', __name__)

@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    """POST endpoint that looks for a supplied string called "url", 
    contained inside a json object. Then validates this url and
    either returns an error response as appropriate, or generates a
    shortened url, stores the shortened url, and then returns it - if valid.
    Parameters:
    None. However, the global request object should contain the aforementioned json.
    Return values:
    A response signifying success or error.
    Successes contain the shortened url and the original one, errors contain an appropriate message.
    """

    data = request.get_json()

    if not data:
        return bad_request('Request must be provided in json format.')
    
    if 'url' not in data:
        return bad_request('Url parameter not found.')

    url_to_shorten = providerShort(data)

    if not provider_valid(url_to_shorten.provider):
      return bad_request('The Provided provider string is not valid. Please try again.')

    if not url_valid(url_to_shorten.url):
      return bad_request('The provided url is not valid. Please try again.')
    
    final_response = url_to_shorten.short_link()

    return jsonify(final_response), 200


@api.route('/shortlinks', methods=['GET'])
def create_shortlink_get():
    """GET endpoint that provides a more useful error message for when
    a user of the api tries to shorten a url through GET.
    Parameters:
    None.
    Return values:
    A response with an appropriate error message and a 400 code.
    """
    return bad_request("Only POST method works!")