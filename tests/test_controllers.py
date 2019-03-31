from unittest.mock import patch
import pytest

from app.controllers import validate_iban
from app.exceptions import InvalidIBANError


def test_validate_iban_raises_invalid_iban_error():
    """
    Test passing invalid IBAN value to the validate_iban controller raises
    InvalidIBANError.
    """
    iban = 'INVALID_IBAN'

    with pytest.raises(InvalidIBANError):
        validate_iban(iban)


def test_validate_iban_calls_schwifty_iban_function():
    """
    Test passing a valid IBAN value to the validate_iban controller will call
    schwifty IBAN function.
    """
    iban = 'DX89 3704 0044 0532 0130 00'

    with patch('app.controllers.IBAN') as PatchedIBAN:
        validate_iban(iban)
        PatchedIBAN.assert_called_once_with(iban)
