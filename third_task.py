import re

phone_1 = "+38(050)11 11 111      "
phone_2 = "    0660750179"

def normalize_phone(phonenumber):
    phonenumber_strip = str.strip(phonenumber)
    pattern = r"[^\d+]"
    phone_norm = re.sub(pattern, "", phonenumber_strip)
    if phone_norm.startswith("+38"):
        return phone_norm
    else:
        phone_with_code = "+38" + phone_norm
        return phone_with_code

print(normalize_phone(phone_1))
print(normalize_phone(phone_2))
