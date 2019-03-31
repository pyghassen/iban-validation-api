from sanic import Sanic
from sanic.response import json

from app.controllers import validate_iban
from app.exceptions import InvalidIBANError

http_server = Sanic()

@http_server.route("/health")
def health_view(request):
    return json({"status": "ok"})


@http_server.route("/iban/validate/<iban>")
def validate_iban_view(request, iban):
    try:
        validate_iban(iban)
    except InvalidIBANError:
        return json({"valid_iban": False}, status=400)

    return json({"valid_iban": True})
