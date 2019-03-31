# IBAN Validation API Service

Purpose
========
IBAN Validation is a micro service which exposes a restful API to check whether the sent IBAN is valid or not.

How to start
===============

0. Prerequisites

   In order to run this project please make sure that the following packages are installed:

       - git
       - docker
       - docker-compose

1. Clone the repository

    `git clone git@github.com:pyghassen/iban-validation-api.git`

2. Run the tests

    `./test.sh`

3. Start the server

    `./run.sh`

4. Send request to the server

    `./send_test_requests.sh`

API reference
=============

1. Health check

    Request:

        GET /health

    + Response 200 (application/json)

        + body

            {"status": "OK"}

2. Validate IBAN

    Request:

        GET /iban/validate/{iban}

    + Response 200 (application/json)

        + body

            {"valid_iban": true}

    + Response 400 (application/json)

        + body

            {"valid_iban": false}

Common Issues
=============

1. Failing to build the container:

    ```
    Building test
    ERROR: Error processing tar file(exit status 1): unexpected EOF
    ```

Just run the following command:

    `./clean.sh`
