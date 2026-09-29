# Decimal to Binary Converter

A simple Python command-line tool that converts decimal numbers to binary and binary numbers back to decimal.

## Features

- Convert decimal numbers to binary.
- Convert binary numbers to decimal.
- Interactive command-line menu.
- Continue performing conversions without restarting the program.
- Validate decimal input.
- Validate binary input.
- Handle empty binary input.
- Provide an option to exit the program.

## Requirements

- Python 3.11 or compatible Python version

No external Python packages are required.

## Usage

Run the program with:

    python decimal_to_binary.py

The program displays three options:

    1. Decimal to Binary
    2. Binary to Decimal
    3. Exit

### Decimal to Binary

Choose option `1` and enter a non-negative decimal integer.

Example:

    Choose an option (1, 2, or 3): 1
    Enter a decimal number: 16
    Binary: 10000

### Binary to Decimal

Choose option `2` and enter a binary number containing only `0` and `1`.

Example:

    Choose an option (1, 2, or 3): 2
    Enter a binary number: 10000
    Decimal: 16

### Exit

Choose option `3` to close the program.

    Choose an option (1, 2, or 3): 3
    Goodbye!

## Input Validation

The program handles invalid inputs such as:

- Negative decimal numbers.
- Empty binary input.
- Binary values containing characters other than `0` and `1`.
- Invalid menu options.
- Non-numeric input where a number is expected.

## Project Structure

    Decimal-to-Binary-Converter/
    │
    ├── decimal_to_binary.py
    ├── README.md
    └── LICENSE

## How It Works

The program provides two conversion functions:

- `decimal_to_binary()` converts a decimal integer into its binary representation.
- `binary_to_decimal()` converts a valid binary string into its decimal value.

The main program provides an interactive menu and continues running until the user selects the exit option.

## Technologies Used

- Python
- Command-line interface
- `bin()` for decimal-to-binary conversion
- `int(..., 2)` for binary-to-decimal conversion

## Author

**Hrishikesh Sharma**

GitHub: RaavanHrishi07

## License

This project is licensed under the MIT License.