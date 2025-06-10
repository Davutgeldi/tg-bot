from aiogram import types

from email_validator import validate_email, EmailNotValidError


def valid_email(text: str) -> str | None:
    try:
        email = validate_email(text)
    except EmailNotValidError:
        return None

    return email.normalized.lower()
