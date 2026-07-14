# ============================================
# VALIDATION FUNCTIONS
# ============================================

def is_valid_phone(phone):
    """
    Validate that the phone number contains exactly 10 digits.
    """
    return phone.isdigit() and len(phone) == 10


def is_valid_email(email):
    """
    Simple email validation.
    """
    return "@" in email and "." in email


def phone_exists(phone, contacts):
    """
    Check whether a phone number already exists.
    """
    for details in contacts.values():
        if details["Phone"] == phone:
            return True
    return False