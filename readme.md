# Random Password Generator

This project is a Python-based application that generates random passwords of user-specified lengths. It combines ease of use with flexibility, allowing customization of the character set used for password creation.

## Features

- **Random Password Generation**: Generates a password using random characters from the set `abc@0123456789`.
- **Custom Length**: Users can specify the desired length of the password.
- **Error Handling**: Gracefully handles invalid inputs, such as non-numeric or negative values.
- **Secure and Random**: Uses Python's `random.choices()` for generating passwords with equal probability for each character.

## How to Run

1. Save the script as `password_generator.py`.
2. Run the script in a terminal or an IDE:
   ```bash
   python password_generator.py
