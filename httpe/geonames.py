import logging
import requests

def call_geonames(q: str, lat: float = None, lng: float = None) -> dict:
    """
    Query the Geonames API with search string & defaults.

    :param q: The search string for the city.
    :param lat: Latitude (optional) to filter results based on the caller's location.
    :param lng: Longitude (optional) to filter results based on the caller's location.
    :return: JSON response from the Geonames API.
    """
    try:
        # Construct the URL for the Geonames API with the provided search query and default parameters.
        url = f'http://api.geonames.org/searchJSON?name_startsWith={q}&country=CA,US&fcode=ppl&'

        # If latitude is provided, add it to the URL.
        if lat:
            url += f'lat={lat}&'

        # If longitude is provided, add it to the URL.
        if lng:
            url += f'lng={lng}&'

        # Append the username parameter to the URL (in this case, it is 'srivalli9726').
        url += 'username=srivalli9726'

        # Log the Geonames API URL that will be called for this query.
        logging.info('Calling Geonames API : %s', url)

        # Make a GET request to the Geonames API with the constructed URL.
        response = requests.get(url)

        # Check the response status code for any errors. If not 200 (OK), raise an HTTPError.
        if response.status_code != 200:
            raise requests.HTTPError(response.status_code)

        # Parse the JSON response from the API and return it.
        return response.json()

    except Exception as e:
        # If there is any exception while calling the API, log the error and raise it.
        logging.error('Error while calling Geonames API : %s', str(e))
        raise e
