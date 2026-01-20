import re
from luhn import luhn_check

# Demo state and registry codes
STATE_CODES = ["05", "09", "14", "23", "28", "19", "21"]
REGISTRY_CODES = ["01", "02", "03", "04", "05"]

def validate_nigeria_id(nid: str) -> bool:
    """
    Returns True if Nigeria Service ID is valid
    """
    # Structure check
    pattern = r"NSV-(\d{2})-(\d{2})-(\d{4})-(\d{4})-(\d)"
    match = re.fullmatch(pattern, nid)
    if not match:
        return False

    state_code, registry_code, year, seq, check_digit = match.groups()

    # Validate state and registry codes
    if state_code not in STATE_CODES or registry_code not in REGISTRY_CODES:
        return False

    # Validate year (2020–2026 for demo)
    if int(year) < 2020 or int(year) > 2026:
        return False

    # Validate sequence (0001–9999)
    if int(seq) < 1 or int(seq) > 9999:
        return False

    # Validate Luhn checksum
    digits_only = ''.join(filter(str.isdigit, nid))
    return luhn_check(digits_only)
