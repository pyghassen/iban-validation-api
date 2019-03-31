from schwifty import IBAN

from app.exceptions import InvalidIBANError


def validate_iban(iban: str):
    try:
        IBAN(iban)
    except ValueError as e:
        raise InvalidIBANError('Invalid IBAN')
