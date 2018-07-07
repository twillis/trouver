from pyramid.config import Configurator


def make_app(settings):
    with Configurator(settings=settings) as config:
        config.include(include_me)
        return config.make_wsgi_app()


def include_me(config):
    config.include('pyramid_jinja2')
    config.add_route('search', '/')
    config.add_route('get', '/get')
    config.add_static_view('assets', 'assets')
    config.scan('.web_views')
