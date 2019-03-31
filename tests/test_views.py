from unittest.mock import Mock

from app.views import health


def test_health_returns_expected_message():
    """
    Test health view return the expected message.
    """
    expected_message = '{"status":"ok"}'
    mocked_request = Mock()

    response = health(mocked_request)

    assert response.status == 200
    assert expected_message == response.body.decode()
