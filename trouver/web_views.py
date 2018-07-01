from pyramid.view import view_config
from .document import Document


@view_config(route_name='search', renderer='templates/search.jinja2')
def search(request):
    return {}
