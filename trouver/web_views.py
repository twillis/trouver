from pyramid.view import view_config
from .document import Document
from pyramid.response import FileResponse

@view_config(route_name='search', renderer='templates/search.jinja2')
def search(request):
    q = request.params.get('q', None)
    s = Document.search()
    s = s.query('match', content=q)
    return {'results': s.execute(), 'q': q}


@view_config(route_name="get", request_method="GET")
def get(request):
    id = request.params.get('id', None)
    doc = Document.get(id=id)
    if doc:
        return FileResponse(id)
