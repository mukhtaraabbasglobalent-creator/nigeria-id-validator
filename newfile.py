# 🇳🇬 Nigeria Service ID Validator + Demo ID Generator

# Luhn Algorithm Functions
def luhn_check(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    checksum = 0
    reverse_digits = digits[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

def calculate_luhn(number: str) -> int:
    digits = [int(d) for d in number if d.isdigit()]
    checksum = 0
    reverse_digits = digits[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return (10 - (checksum % 10)) % 10

# Demo state and registry codes
STATE_CODES = ["05", "09", "14", "23", "28", "19", "21"]
REGISTRY_CODES = ["01", "02", "03", "04", "05"]

# Years and sequences for demo
YEARS = ["2025", "2026"]
SEQUENCES = ["0001", "0123", "0456"]

# Function to generate valid IDs
def generate_nigeria_id(state, registry, year, seq):
    partial_id = f"NSV-{state}-{registry}-{year}-{seq}"
    check_digit = calculate_luhn(partial_id)
    return f"{partial_id}-{check_digit}"

# Generate demo IDs
print("🇳🇬 Generated Nigeria Demo IDs\n")
demo_ids = []
for state in STATE_CODES[:3]:
    for registry in REGISTRY_CODES[:3]:
        for year in YEARS:
            for seq in SEQUENCES:
                nid = generate_nigeria_id(state, registry, year, seq)
                demo_ids.append(nid)
                print(nid)

# Validator Function
import re
def validate_nigeria_id(nid: str) -> bool:
    pattern = r"NSV-(\d{2})-(\d{2})-(\d{4})-(\d{4})-(\d)"
    match = re.fullmatch(pattern, nid)
    if not match:
        return False
    state_code, registry_code, year, seq, check_digit = match.groups()
    if state_code not in STATE_CODES or registry_code not in REGISTRY_CODES:
        return False
    if int(year) < 2020 or int(year) > 2026:
        return False
    if int(seq) < 1 or int(seq) > 9999:
        return False
    digits_only = ''.join(filter(str.isdigit, nid))
    return luhn_check(digits_only)

# Console for user input
print("\n🇳🇬 Nigeria Service ID Validator Demo\n")
while True:
    nid_input = input("Enter Nigeria Service ID (or 'q' to quit): ")
    if nid_input.lower() == "q":
        break
    if validate_nigeria_id(nid_input):
        print("✅ ID is valid!\n")
    else:
        print("❌ ID is invalid!\n")