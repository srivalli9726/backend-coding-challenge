from flask import Blueprint, request
from flask_apispec import doc

from impl.suggestions import get_suggestions

suggestions_bp = Blueprint('suggestions', __name__)


@doc
@suggestions_bp.route('/suggestions', methods=['GET'])
# @use_kwargs(Suggestions, location='query')  # request param validation
# @marshal_with(SuggestionsResponse)
def suggestions_call() -> dict:
    args = request.args
    return get_suggestions(args['q'], args.get('lat'), args.get('lng'))
