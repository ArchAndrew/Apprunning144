from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    Andrew = os.environ.get('ANDREW')
    if Andrew == None or len(Andrew) == 0:
        Andrew = "world"
    message = "You have now left The Matrix, " + Andrew + "!\n"
    return Response(message)

if __Andrew__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_Andrew='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
