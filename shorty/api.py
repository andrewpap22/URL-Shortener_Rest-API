from shorty.custom_shorty.custom import *

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
    if not request.json:
        return bad_request('Url must be provided in json format.')
    
    if 'url' not in request.json:
        return bad_request('Url parameter not found.')
    
    #if 'provider' not in request.json:
    """ if the provider is not given by the user the default tinyurl will be selected. """

    
    url = request.json['url']
    #provider = request.json['provider']

    if not url_valid(url):
        return bad_request('Provided url is not valid. Please try again.')

    shortened_url = shorten(url)
    shortened[shortened_url] = url
    
    return jsonify({
        'url':url,
        'link':shortened_url
    }), 200

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