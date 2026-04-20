def validate_age(age: int) -> True|False:
    return True if age >= 18 else False

def validate_email(email:str) -> True|False:
    return True if "@" in email and "." in email else False
