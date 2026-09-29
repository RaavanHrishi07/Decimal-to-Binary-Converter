def decimal_to_binary(number):
    """Convert a decimal integer to binary."""
    return bin(number)[2:]


def binary_to_decimal(binary_number):
    """Convert a binary number to decimal."""
    return int(binary_number, 2)


def main():
    print("Number Converter")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")

    try:
        choice = int(input("Choose an option (1 or 2): "))

        if choice == 1:
            decimal = int(input("Enter a decimal number: "))

            if decimal < 0:
                print("Please enter a non-negative decimal number.")
                return

            result = decimal_to_binary(decimal)
            print(f"Binary: {result}")

        elif choice == 2:
            binary = input("Enter a binary number: ").strip()

            if not binary or any(digit not in "01" for digit in binary):
                print("Please enter a valid binary number.")
                return

            result = binary_to_decimal(binary)
            print(f"Decimal: {result}")

        else:
            print("Please choose option 1 or 2.")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()