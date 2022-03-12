from django.contrib.auth.hashers import make_password


def encode_password(password: str) -> str:
    """Turn a plain-text password into a hash for database storage"""
    return make_password(password)