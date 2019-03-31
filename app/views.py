from sanic import Sanic
from sanic.response import json

http_server = Sanic()

@http_server.route("/health")
def health(request):
    return json({"status": "ok"})
