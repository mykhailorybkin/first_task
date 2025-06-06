import re

phone_1 = "+38(050)11 11 111      "
phone_2 = "    38050-111-22-22"

def normalize_phone(phonenumber):
    phonenumber_strip = str.strip(phonenumber)
    pattern_without_symbols = r"[^\d+]"
    phone_without_symbols = re.sub(pattern_without_symbols, "", phonenumber_strip)
    pattern_general = r"\+\d{12}"
    if re.fullmatch(pattern_general, phone_without_symbols):
        phone_norm = phone_without_symbols
        return phone_norm
    else:
        if phone_without_symbols.startswith("0"):
            phone_norm = "+38" + phone_without_symbols
            return phone_norm
        elif phone_without_symbols.startswith("38"):
            phone_norm = "+" + phone_without_symbols
            return phone_norm
            

print(normalize_phone(phone_1))
print(normalize_phone(phone_2))
