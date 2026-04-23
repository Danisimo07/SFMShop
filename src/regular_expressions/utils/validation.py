import re


def validate_email_regex(email: str) -> True|False:
    pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
    match = re.fullmatch(pattern, email)
    return match


def validate_phone_regex(phone: str) -> True|False:
    pattern = r"\+7[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}"
    match = re.fullmatch(pattern, phone)
    return match


def clean_input(text: str) -> True|False:
    pattern = r"[^\w\s.]"
    match = re.sub(pattern, "", text)
    return match


def extract_email_from_text(text: str) -> str|None:
    pattern = r"\S+@\S+\.\S+"
    match = re.search(pattern, text)

    if match:
        return match.group()
    else:
        return None
