def decimal_to_binary(number):
    """Convert a non-negative decimal integer to binary."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Decimal input must be an integer.")

    if number < 0:
        raise ValueError("Decimal input cannot be negative.")

    return bin(number)[2:]


def binary_to_decimal(binary_number):
    """Convert a valid binary string to decimal."""
    if not isinstance(binary_number, str):
        raise ValueError("Binary input must be a string.")

    binary_number = binary_number.strip()

    if not binary_number:
        raise ValueError("Binary input cannot be empty.")

    if any(digit not in "01" for digit in binary_number):
        raise ValueError("Binary input can contain only 0 and 1.")

    return int(binary_number, 2)
    