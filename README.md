# IBAN Validation API Service

Purpose
========
IBAN Validation is a micro service which exposes a restful API to check whether the sent IBAN is valid or not.

How to start
===============

1. Clone the repository

`git clone git@github.com:pyghassen/iban-validation-api.git`

2. Start the server

`./run.sh`

3. Send request to the server

`./send_request.sh`

API reference
=============

1. Health check

# Request:

## GET /health

+ Response 200 (application/json)

    + body

        {"status": "OK"}

2. Validate IBAN

# Request:

## GET /iban/validate/{iban}

+ Response 200 (application/json)

    + body

        {"valid": true}

+ Response 400 (application/json)

    + body

        {"valid_iban": false}
