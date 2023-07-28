import logging
from httpe.geonames import call_geonames


def get_score(geoname: dict) -> float:
    """
    Calculates the score for a given geoname.

    Args:
        geoname: The geoname to calculate the score for.

    Returns:
        The score for the geoname.
    """

    score = 0.9  # Initial score.
    score += 0.1 * geoname['population']  # Add 10% of the population to the score.
    score -= 0.01 * (geoname['distance'] / 1000)  # Subtract 1% of the distance from the score.
    return score  # Return the score.


def get_suggestions(q: str, lat: float = None, lng: float = None) -> dict:
    """
    Gets the suggestions for a given search query.

    Args:
        q: The search query.
        lat: The user's latitude.
        lng: The user's longitude.

    Returns:
        A dictionary of suggestions.
    """

    try:
        suggestions = []  # Initialize the list of suggestions.
        geonames = call_geonames(q, lat, lng)  # Get the geonames from the GeoNames API.
        if 'geonames' in geonames:  # Check if the geonames response contains any results.
            sorted_geonames = sorted(geonames['geonames'], key=lambda g: get_score(g))  # Sort the geonames by score.
            if sorted_geonames:  # Check if the sorted geonames list is not empty.
                logging.info(f'Processing {len(sorted_geonames)} suggestion(s) from Geonames API')
                for geoname in sorted_geonames:
                    suggestion = {
                        'name': geoname['name'] + ", " + geoname['adminCodes1']['ISO3166_2'] + ", " + geoname[
                            'countryName'],  # Create a suggestion object.
                        'latitude': geoname['lat'],
                        'longitude': geoname['lng'],
                        'score': get_score(geoname),
                        'link': f'https://en.wikipedia.org/wiki/{geoname["name"]}'
                    }
                    suggestions.append(suggestion)  # Add the suggestion to the list of suggestions.
        if suggestions:  # Check if the suggestions list is not empty.
            logging.info(f'Returning {len(suggestions)} suggestion(s)')
        return {'suggestions': suggestions}  # Return the suggestions.
    except Exception as e:
        logging.error('Error while processing Geonames response : %s', str(e))
        raise e

