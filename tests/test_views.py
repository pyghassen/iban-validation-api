from unittest.mock import Mock

from app.views import health_view, validate_iban_view


def test_health_returns_expected_success_message():
    """
    Test health view return the expected message.
    """
    expected_message = '{"status":"ok"}'
    mocked_request = Mock()
    response = health_view(mocked_request)

    assert response.status == 200
    assert expected_message == response.body.decode()


def test_validate_returns_expected_success_message():
    """
    Test health view return the expected message.
    """
    expected_message = '{"valid_iban":true}'
    mocked_request = Mock()

    iban = 'DE89 3704 0044 0532 0130 00'

    response = validate_iban_view(mocked_request, iban)

    assert response.status == 200
    assert expected_message == response.body.decode()
