import re

def validate_email(email):
    EMAIL_REGEX = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
    if not re.match(EMAIL_REGEX, email):
        raise

def validate_password(password):
    PASSWORD_REGEX = "^(?=.*[a-zA-Z])(?=.*[!@#$%^~*+=-])(?=.*[0-9]).{8,}$"
    return re.match(PASSWORD_REGEX, password)
