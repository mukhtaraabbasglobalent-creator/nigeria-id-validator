def luhn_check(number: str) -> bool:
    """
    Returns True if number passes Luhn checksum
    """
    digits = [int(d) for d in number if d.isdigit()]
    checksum = 0
    reverse_digits = digits[::-1]

    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:  # Double every second digit from the right
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

    return checksum % 10 == 0


def calculate_luhn(number: str) -> int:
    """
    Calculate Luhn check digit for a number without check digit
    """
    digits = [int(d) for d in number if d.isdigit()]
    checksum = 0
    reverse_digits = digits[::-1]

    for i, digit in enumerate(reverse_digits):
        if i % 2 == 0:  # For calculation, double every second digit differently
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

    return (10 - (checksum % 10)) % 10
