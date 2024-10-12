import re

def normalize_phone(phone_number):
    only_numbers=re.sub(r"\D+","",phone_number)
    if len(only_numbers)==10:
        normalize_phone_number="+38"+only_numbers
        print(normalize_phone_number)
        return normalize_phone_number
    elif len(only_numbers)==12:
        normalize_phone_number = "+" + only_numbers
        print(normalize_phone_number)
        return normalize_phone_number
    else:
        print("Invalid value")
        return "Invalid value"

normalize_phone("067\\t123 4567")