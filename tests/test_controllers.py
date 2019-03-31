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
